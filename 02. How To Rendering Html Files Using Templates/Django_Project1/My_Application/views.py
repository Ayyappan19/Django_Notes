from django.shortcuts import render

from django.http import HttpResponse
from pathlib import Path
import os
BASE_DIR = Path(__file__).resolve().parent.parent
# Create your views here.


def home(request):
    result = os.path.join(BASE_DIR,"Templates")
    print(result)
    return render(request,"index.html")
