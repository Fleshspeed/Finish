from django.shortcuts import render, redirect, get_object_or_404
from .models import User
from.forms import UserForm

def index(request):
    items = User.objects.all()
    return render(request, 'app/index.html', {'items':items})

def list(request):
    items = User.objects.all()  
    return render(request, 'app/list.html', {'items': items})


def create(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list')
    else:
        form = UserForm()
    return render(request, 'app/form.html', {'form': form})


def update(request, pk):
    item = get_object_or_404(User, pk=pk)  
    if request.method == 'POST':
        form = UserForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('list')
    else:
        form = UserForm(instance=item) 
    return render(request, 'app/update.html', {'form': form})





def delete(request, pk):
    item = get_object_or_404(User, pk=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('list')
    return render(request, 'app/delete.html', {'item': item})

