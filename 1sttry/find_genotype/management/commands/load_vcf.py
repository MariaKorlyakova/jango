from find_genotype.models import Genotype
from django.core.management.base import BaseCommand, CommandError
from pathlib import Path
from django.db import transaction
import gzip

def dot_to_none(arg, to_type=str):
    if arg == ".":
        return None
    return to_type(arg)
    
def islice(iterator, batch_size):
    batch = []
    for i in iterator:
        batch.append(i)
        if len(batch) == batch_size:
            return batch
    return batch

def iter_genotypes(file):
    for n, line in enumerate(file, start=1):
        line = line.rstrip()
        if not line.startswith("#") and line:
            line_parsed = line.split("\t")
            if len(line_parsed) != 10:
                raise CommandError(f"Got {len(line_parsed)} columns in line {n}, expected 10.")
            chrom,pos,uid,ref,alt,qual,filt,inf,form,hg001 = line_parsed
            parsed_format = dict(zip(form.split(":"), hg001.split(":")))
            pos = int(pos)
            genot = dot_to_none(parsed_format.get("GT", "."))
            ps = dot_to_none(parsed_format.get("PS", "."), int)
            dp = dot_to_none(parsed_format.get("DP", "."), int)
            adall = dot_to_none(parsed_format.get("ADALL", "."))
            ad = dot_to_none(parsed_format.get("AD", "."))
            gq = dot_to_none(parsed_format.get("GQ", "."), int)
            yield Genotype(chrom=chrom, pos=pos, uid=dot_to_none(uid), ref=ref, alt=dot_to_none(alt), qual=dot_to_none(qual, float),
                           filter=dot_to_none(filt), info=dot_to_none(inf), gt=genot, phase_set=ps,
                           depth=dp, allel_depth_all=adall, allel_depth_nofilt=ad, genotype_quality=gq)

class Command(BaseCommand):
    help = "Extract vcf file and pull it into Genotype model."
    
    def add_arguments(self, parser):
        parser.add_argument("path_to_vcf", help="Enter path to vcf file")
        
    def handle(self, *args, **options):
        path_to_vcf = Path(options["path_to_vcf"])
        if not path_to_vcf.is_file():
            raise CommandError(f"File {path_to_vcf} does not exist.")
        if path_to_vcf.suffix == ".gz":
            open_vcf = gzip.open
        else:
            open_vcf = open

        with open_vcf(path_to_vcf, "rt") as vcf:
            gen_iter = iter_genotypes(vcf)
            total_add = 0
            with transaction.atomic():
                while True:
                    batch_for_load = islice(gen_iter, 3000)
                    if not batch_for_load:
                        break
                    Genotype.objects.bulk_create(batch_for_load)
                    total_add += len(batch_for_load)
                    self.stdout.write(f"Loaded {total_add}")
            self.stdout.write(self.style.SUCCESS(f"All {total_add} genotypes loaded."))