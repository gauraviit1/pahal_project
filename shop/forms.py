from dal import autocomplete

from django import forms
from shop.models import Cateogry, Product


class CateogryForm(forms.ModelForm):
    name = forms.ModelChoiceField(
        queryset=Cateogry.objects.all(),
        widget=autocomplete.ModelSelect2(url='shop:cateogry-autocomplete')
    )

    class Meta:
        model = Product
        fields = ('__all__')