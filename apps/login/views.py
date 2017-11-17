from django.shortcuts import render

# Create your views here.
def index(request):
    try:
        request.session['total']
    except KeyError:
        request.session['total'] = 0
    return render(request, "login/index.html")
