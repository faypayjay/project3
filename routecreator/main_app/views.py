from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView

# Add the following import
from django.http import HttpResponse
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required # for function definitions, not CBV
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Route, Photo

# Define the home view
def home(request):
  return HttpResponse('<h1>Hello /ᐠ｡‸｡ᐟ\ﾉ</h1>')
# Create your views here.

def about(request):
    return render(request, 'about.html')

class RouteList(ListView):
  model = Route