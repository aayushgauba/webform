from django.shortcuts import render, redirect
from .models import Chain
from django_countries.data import COUNTRIES

def data(request):
    chain = Chain.objects.all()
    return render(request, "data.html", context={"chains":chain})

def index(request):
    if request.method == "POST":
        name = request.POST.get("name")
        profession = request.POST.get("profession")
        city = request.POST.get("city")
        country = request.POST.get("country")
        animal= request.POST.get("animal")
        contact= request.POST.get("contact")
        comment = request.POST.get("comment")
        volunteer = request.POST.get("volunteer")
        if volunteer == None:
            volunteer = False
        else:
            volunteer = True
        Chain.objects.create(birdType=animal, name=name, profession=profession, city=city, country= country, activeVolunteer=volunteer, contact=contact, comments =comment)
        return redirect("index")
    return render(request, "index.html", context={"countries":list(COUNTRIES.values())})