from django.db import models
    
class Genotype(models.Model):
    chrom = models.TextField()
    pos = models.IntegerField()
    uid = models.TextField(null=True)
    ref = models.TextField()
    alt = models.TextField(null=True)
    qual = models.FloatField(null=True)
    filter = models.TextField(null=True)
    info = models.TextField(null=True)
    gt = models.TextField(null=True)
    phase_set = models.IntegerField(null=True)
    depth = models.IntegerField(null=True)
    allel_depth_all = models.TextField(null=True)
    allel_depth_nofilt = models.TextField(null=True)
    genotype_quality = models.IntegerField(null=True)
    
    class Meta:
        indexes = [models.Index(fields=["chrom", "pos"]),]
