from django.shortcuts import render
from katalog.models import CatalogItem

# Create request parameter.
def show_katalog(request):
    data_barang_katalog = CatalogItem.objects.all()
    context = {
        'list_barang': data_barang_katalog,
        'nama': 'Kevin Alexander',
        'studentid': '2106705026'
    }
    return render(request, "katalog.html", context)