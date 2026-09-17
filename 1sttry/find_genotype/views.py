from django.shortcuts import render
from .models import Genotype
from .forms import GenotypeRequestForm

def find_genotype(request):
    form = GenotypeRequestForm(request.GET or None)
    genotypes = None
    if form.is_valid():
        f = form.cleaned_data
        genotypes = Genotype.objects.filter(pos__range=(f["start"], f["end"]), chrom=f["chrom"])
    return render(request, "find_genotype/find_genotype.html", {"genotypes": genotypes, "form": form})
    

