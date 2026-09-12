from django.conf import settings
from django.db import models

#class FindGenotypeManager(models.Manager):
#    def get_queryset(self):
#        return super().get_queryset().filter(pos__range=(QueryGenotype.startpos, QueryGenotype.endpos), chrom=QueryGenotype.chromquery)
    
class Genotype(models.Model):
    chrom = models.TextField()
    pos = models.IntegerField()
    uid = models.TextField()
    ref = models.TextField()
    alt = models.TextField()
    qual = models.FloatField()
    filter_status = models.TextField()
    info = models.TextField()
    genotype_format = models.TextField()
    genotype_id = models.TextField()
#    find_genotype = FindGenotypeManager()

# class QueryGenotype(models.Model):
#     genotype = models.ForeignKey(Genotype)
#     chromquery = models.TextField()
#     startpos = models.IntegerField()
#     endpos = models.IntegerField()