from django.shortcuts import render
from .forms import ComputerForm
from .models import Computer

# Create your views here.
def home(request):
    title = 'Welcome: This is the Home Page'
    context = {
        "title": title,
    }
    return render(request, "home.html", context)

def computer_entry(request):
    title = "Add Computer"
    form = ComputerForm(request.POST or None)
    
    if form.is_valid():
        form.save()
    
    context = {
        "title": title,
        "form": form,
    }
    
    return render(request, "computer_entry.html", context)

def computer_list(request):
    title = 'List of all computers'
    queryset = Computer.objects.all()
    context = {
        "title": title,
        "queryset": queryset,
    }
    return render(request, "computer_list.html",context)