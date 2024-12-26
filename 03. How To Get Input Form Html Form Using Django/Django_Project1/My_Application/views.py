from django.shortcuts import render

from django.http import HttpResponse
# from pathlib import Path
# import os
# BASE_DIR = Path(__file__).resolve().parent.parent
# Create your views here.


def home(request):
    return render(request,"index.html")


def product(request):

    Mobile = int(request.GET["mobile"])
    Keyboard = int(request.GET["keyboard"])
    Monitor = int(request.GET["monitor"])

    price = Mobile + Keyboard + Monitor

    return render(request,"Result.html",{'Price':price})