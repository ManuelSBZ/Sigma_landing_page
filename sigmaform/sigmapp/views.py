from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from .forms import SignForm


# Create your views here.

def person_create_view(request):
    form = SignForm()
    if request.method == 'POST':
        form = SignForm(request.POST)
        if form.is_valid():
            print("OK")
            return HttpResponse("OK")

    return render(request, 'index.html', {'form': form})