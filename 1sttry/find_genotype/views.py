from django.shortcuts import render
from .models import Genotype

def find_genotype(request):
    genotypes = Genotype.objects.filter(pos__range=(startpos, endpos), chrom=chromquery)
    return render(request, 'find_genotype/find_genotype.html', {'genotypes': genotypes})


