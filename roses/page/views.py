from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect

 # from .models import Question


def index(request):

    return render(request, 'page/index.html')