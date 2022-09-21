from django.shortcuts import render
from mywatchlist.models import MyWatchList
from django.http import HttpResponse
from django.core import serializers

# Create your views here.
def show_mywatchlist(request):
    context = {
        'nama': 'Kevin Alexander',
        'studentid': '2106705026',
    }
    return render(request, "mywatchindex.html", context)

def show_xml(request):
    data = MyWatchList.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = MyWatchList.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_html(request):
    data_watchlist = MyWatchList.objects.all()
    dataTonton = data_watchlist.filter(watched=True)
    dataTidak = data_watchlist.filter(watched=False)
    context = {
        'watch_list': data_watchlist,
        'tonton': dataTonton,
        'tidak_tonton': dataTidak,
        'nama': 'Kevin Alexander',
        'studentid': '2106705026',
    }
    return render(request, "mywatchlist.html", context)

def show_json_by_id(request, id):
    data = MyWatchList.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = MyWatchList.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_html_by_id(request, id):
    data_watchlist = MyWatchList.objects.filter(pk=id)
    context = {
        'watch_list': data_watchlist,
        'nama': 'Kevin Alexander',
        'studentid': '2106705026',
    }
    return render(request, "mywatchlist.html", context)