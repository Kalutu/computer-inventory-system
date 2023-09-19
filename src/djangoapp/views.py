from django.shortcuts import render, redirect
from .forms import ComputerForm, ComputerSearchForm
from .models import Computer
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
import csv

# Create your views here.
def home(request):
    title = 'Welcome: This is the Home Page'
    context = {
        "title": title,
    }
    return render(request, "base.html", context)

def computer_entry(request):
    title = "Add Computer"
    form = ComputerForm(request.POST or None)
    
    if form.is_valid():
        computer = form.save(commit=False) 
        computer.save() 
        form.save_m2m() 
        messages.success(request, 'Successfully Saved')
        return redirect('/computer_list')
    context = {
        "title": title,
        "form": form,
    }
    
    return render(request, "computer_entry.html", context)

def computer_list(request):
    title = "List of all computers"
    form = ComputerSearchForm(request.POST or None)
    
    
    if request.method == 'POST':
        queryset = Computer.objects.all().order_by('-timestamp').filter(computer_name__icontains=form['computer_name'].value(), users_name__icontains=form['users_name'].value())
    else:
        queryset = Computer.objects.all()
    context = {
        "title": title,
        "queryset": queryset,
        "form": form,
    }
    if form['export_to_CSV'].value() == True:
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="Computer list.csv"'
        writer = csv.writer(response)
        writer.writerow(['COMPUTER NAME', 'IP Address', 'MAC ADDRESS', 'OS', 'USERNAME', 'LOCATION', 'PURCHASE DATE', 'TIMESTAMP'])
        instance = queryset
        for row in instance:
            writer.writerow([row.computer_name, row.IP_address, row.MAC_address, row.operating_system.all(), row.users_name, row.location, row.purchase_date, row.timestamp])
        return response
    return render(request, "computer_list.html",context)

def computer_edit(request, id=None):
    instance = get_object_or_404(Computer, id=id)
    form = ComputerForm(request.POST or None, instance=instance)

    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        form.save_m2m()
        messages.success(request, 'Successfully Saved')
        return redirect('/computer_list')

    context = {
        "title": 'Edit ' + str(instance.computer_name),
        "instance": instance,
        "form": form,
    }
    return render(request, "computer_entry.html", context)

def computer_delete(request, id=None):
   instance = get_object_or_404(Computer, id=id)
   instance.delete()
   return redirect("computer_list")





