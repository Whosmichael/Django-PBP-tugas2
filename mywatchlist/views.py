from django.shortcuts import render
from mywatchlist.models import watchlists
from django.core import serializers
from django.http import HttpResponse
# Create your views here.

pesan =''
parameter = 0
watchlist_data = watchlists.objects.all()

for items in watchlist_data:
    if(items.watched == "Yes"):
        parameter += 1
    
if(parameter < 10 - parameter):
    message="Wah, kamu masih sedikit menonton!"
else:
    message="Selamat, kamu sudah banyak menonton!"

context = {
    'watch_list': watchlist_data,
    'nama': 'Michael Baptiswa',
    'npm' : '2106752054',
    'pesan' : message
}

def show_mywatchlist(request):
    watchlist_data = watchlists.objects.all()
    return render(request, "watchlist.html", context)

def show_xml(request):
    data = watchlists.objects.all()
    return HttpResponse(serializers.serialize('xml', data), content_type="application/xml")

def show_json(request):
    data = watchlists.objects.all()        
    return HttpResponse(serializers.serialize('json', data), content_type="application/json")

def show_json_by_id(request, id):
    data = watchlists.objects.filter(pk=id)
    return HttpResponse(serializers.serialize('json', data), content_type="application/json")

def show_xml_by_id(request, id):
    data = watchlists.objects.filter(pk=id)
    return HttpResponse(serializers.serialize('xml', data), content_type="application/xml")