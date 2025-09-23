from django.shortcuts import render
from .models import *
# Create your views here.


# -----------------------------------Public functions----------------------------------

def index(request):
    return render(request,'public/index.html')