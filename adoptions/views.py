from django.shortcuts import render
from django.http import HttpResponse, Http404

from .models import Pet

# Create your views here.
def home(request):
    pets = Pet.objects.all()
    return render(request, "home.html", {"pets": pets})


def pet_details(request, id):
    try:
        pet = Pet.objects.get(id=id)
    except Pet.DoesNotExists:
        raise Http404("Pet not found")
    return render(request, "pet_details.html", {"pet": pet})
