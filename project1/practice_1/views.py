from django.shortcuts import render
from .models import Item

def home(request):
    items = Item.objects.all()
    return render(request, "practice_1/home.html", {"items": items})
