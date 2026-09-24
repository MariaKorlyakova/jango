from django.shortcuts import render
from .models import Genotype
from .forms import GenotypeRequestForm

def find_genotype(request):
    form = GenotypeRequestForm(request.GET or None)
    genotypes = None
    if form.is_valid():
        f = form.cleaned_data
        genotypes = Genotype.objects.select_related("coordinate__chromosome", "sample").filter(coordinate__pos__range=(f["start"], f["end"]), coordinate__chromosome__chrom=f["chrom"])
        if f["sample"] is not None:
            genotypes = genotypes.filter(sample=f["sample"])
    return render(request, "find_genotype/find_genotype.html", {"genotypes": genotypes, "form": form})
    

