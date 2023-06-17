from django.shortcuts import render

def index(request):
    return render(request,'ksan/KSAN.html')

def about(request):
    return HttpResponse("<h1>Zdarovo</h1>")


