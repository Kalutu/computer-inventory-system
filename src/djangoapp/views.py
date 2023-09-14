from django.shortcuts import render
from .forms import ComputerForm

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
