from django.shortcuts import render, get_object_or_404
from shop.models import Cateogry, Product
from cart.forms import CartAddProductForm

# Create your views here.
def product_list(request, cateogry_slug=None):
    cateogry = None
    cateogries = Cateogry.objects.all()
    products = Product.objects.filter(available=True)
    if cateogry_slug:
        cateogry = get_object_or_404(Cateogry,slug=cateogry_slug)
        products = products.filter(cateogry=cateogry)
    return render(request, 'shop/product/list.html', {
        'cateogry': cateogry,
        'cateogries': cateogries,
        'products': products,
    })

def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id,
                                     slug=slug,
                                     available=True)
    cart_product_form = CartAddProductForm()
    return render(request, 'shop/product/detail.html',
                  {'product': product,
                   'cart_product_form': cart_product_form})


from dal import autocomplete

from shop.models import Product


class CateogryAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !
        if not self.request.user.is_authenticated():
            return Cateogry.objects.none()

        qs = Cateogry.objects.all()

        if self.q:
            qs = qs.filter(name__istartswith=self.q)

        return qs