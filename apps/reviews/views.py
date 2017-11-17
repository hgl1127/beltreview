# Create your views here.
from django.shortcuts import render, HttpResponse, redirect
  # the index function is called when root is visited

def index(request):
    try:
        request.session['total']
    except KeyError:
        request.session['total'] = 0
    return render(request, "reviews/index.html")
