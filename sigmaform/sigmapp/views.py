from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .forms import SignForm
from .helper import k
from .models import SingIn
import requests
import json


def person_create_view(request):
    form = SignForm()
    if request.method == 'POST':
        form = SignForm(request.POST)
        if form.is_valid():
            data = {key:value for key,value in form.data.items()
                                            if key != "csrfmiddlewaretoken"}
            SingIn.objects.create(**data)
            return HttpResponse("OK")
        else:
            #AJAX
            errors = json.loads(form.errors.as_json())
            return render(request, "errors.html", {"form":form})
    return render(request, 'index.html', {'form': form})

# AJAX
def load_cities(request):
    department_tag = request.GET.get('tag_department')
    collection = k
    cities = collection.get(department_tag, ["No hay ciudades encontradas"])
    return render(request, 'dropdown.html', {'cities': cities})