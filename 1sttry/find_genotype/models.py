from django.db import models
    
class Genotype(models.Model):
    coordinate = models.ForeignKey(
        "Coordinate",
        on_delete=models.CASCADE,
    )
    sample = models.ForeignKey(
        "Sample",
        on_delete=models.CASCADE,
    )
    gt = models.TextField(null=True)
    phase_set = models.IntegerField(null=True)
    depth = models.IntegerField(null=True)
    allel_depth_all = models.TextField(null=True)
    allel_depth_nofilt = models.TextField(null=True)
    genotype_quality = models.IntegerField(null=True)
    
    class Meta:
        constraints = [models.UniqueConstraint(fields=["coordinate", "sample"], name="unique_genotype")]
        
        
class Coordinate(models.Model):
    chromosome = models.ForeignKey(
        "Chromosome",
        on_delete=models.PROTECT,
    )
    pos = models.IntegerField()
    uid = models.TextField(null=True)
    ref = models.TextField()
    alt = models.TextField(null=True)
    qual = models.FloatField(null=True)
    filter = models.TextField(null=True)
    info = models.TextField(null=True)
    
    class Meta:
        constraints = [models.UniqueConstraint(fields=["chromosome", "pos", "ref", "alt"], name="unique_variant")]

class Chromosome(models.Model):
    assembly = models.ForeignKey(
        "Assembly",
        on_delete=models.PROTECT,
    )
    chrom = models.TextField()
    length = models.IntegerField()
    
    class Meta:
        constraints = [models.UniqueConstraint(fields=["assembly", "chrom"], name="unique_chrom")]

class Assembly(models.Model):
    assembly_uid = models.TextField(unique=True)

class Sample(models.Model):
    sample_uid = models.TextField(unique=True)
    file_name = models.TextField()