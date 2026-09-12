from django import forms
from .models import Genotype

class GenotypeRequestForm(forms.ModelForm):

    class Meta:
        model = Genotype
        fields = ('CHROM', 'POS', 'UID', 'REF', 'ALT', 'QUAL', 'FILTER', 'INFO', 'FORMAT', 'HG001',)