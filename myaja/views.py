from django.shortcuts import render
from .models import Articles

# Create your views here.
def accueil(request):
    return render(request,"accueil.html")
def service1(request):
    return render(request,"service1.html")
def service2(request):
    return render(request, "service2.html")
def service3(request):
    return render(request, "service3.html")
def blog(request):
    articles=Articles.objects.all()
    return render(request, "blog.html",locals() )
def register(request):
    return render(request, "register.html")
def team(request):
        return render(request, "team.html")
def blogdetail(request):
     return render(request, "blogdetail.html")
def about(request):
     return render(request, "about.html")


