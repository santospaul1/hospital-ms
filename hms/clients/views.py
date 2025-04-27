from django.shortcuts import render, redirect
from .models import Client
from .forms import ClientForm

def add_client(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_clients')
    else:
        form = ClientForm()
    return render(request, 'clients/add_client.html', {'form': form})

from django.db.models import Q  

def list_clients(request):
    query = request.GET.get('q')
    if query:
        clients = Client.objects.filter(
            Q(full_name__icontains=query) | Q(phone_number__icontains=query)
        )
    else:
        clients = Client.objects.all()
    return render(request, 'clients/list_clients.html', {'clients': clients, 'query': query})

def edit_client(request, client_id):
    client = Client.objects.get(id=client_id)
    if request.method == 'POST':
        form = ClientForm(request.POST, instance=client)
        if form.is_valid():
            form.save()
            return redirect('list_clients')
    else:
        form = ClientForm(instance=client)
    return render(request, 'clients/edit_client.html', {'form': form})

def delete_client(request, client_id):
    client = Client.objects.get(id=client_id)
    if request.method == 'POST':
        client.delete()
        return redirect('list_clients')
    return render(request, 'clients/delete_client.html', {'client': client})
