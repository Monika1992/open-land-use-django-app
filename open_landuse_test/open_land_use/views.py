from django.shortcuts import render
from django.http import HttpResponse
from models import Municipality_area


def index(request):
    query_results = Municipality_area.objects.all()
    return HttpResponse('open land use index site')
    # shows content of table in index page
    # return HttpResponse(query_results)
