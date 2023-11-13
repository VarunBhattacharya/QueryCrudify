from django.http import HttpResponse
from django.shortcuts import render
from crudOp.models import BasicTable

def mainPage(request):
    basicTab = BasicTable.objects.all()
    dataTransfer = {
        'basicTable': basicTab
    }
    return render(request, "index.html", dataTransfer)