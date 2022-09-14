from django.shortcuts import render
from katalog.models import CatalogItem
# Create your views here.
def show_catalog(request):
    return render(request, "Katalog.html", context)
data_barang_katalog = CatalogItem.objects.all()
context = {
    'list_barang': data_barang_katalog,
    'nama': 'Michael Baptiswa',
    'npm' : '2106752054'
}