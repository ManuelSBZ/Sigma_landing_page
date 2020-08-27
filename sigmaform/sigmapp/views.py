from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .forms import SignForm
from .helper import k
import requests
import json


def person_create_view(request):
    form = SignForm()
    if request.method == 'POST':
        print(f"request.POST{request.POST==None}")
        form = SignForm(request.POST)
        print(form.data)
        if form.is_valid():
            return HttpResponse("OK")
        else:
            #AJAX
            errors = json.loads(form.errors.as_json())
            print(errors)
            return render(request, "errors.html", {"form":form})
    return render(request, 'index.html', {'form': form})

# AJAX
def load_cities(request):
    department_tag = request.GET.get('tag_department')
    collection = k
    cities = collection.get(department_tag, ["No cities Found"])
    return render(request, 'dropdown.html', {'cities': cities})