from django.shortcuts import render, redirect
from .models import HealthProgram
from .forms import HealthProgramForm

# View to add a new Health Program
def add_program(request):
    if request.method == 'POST':
        form = HealthProgramForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list-programs')
    else:
        form = HealthProgramForm()
    return render(request, 'programs/add_program.html', {'form': form})

# View to list all Health Programs
from django.db.models import Q

def list_programs(request):
    query = request.GET.get('q')
    if query:
        programs = HealthProgram.objects.filter(
            Q(name__icontains=query) | Q(description__icontains=query)
        )
    else:
        programs = HealthProgram.objects.all()
    return render(request, 'programs/list_programs.html', {'programs': programs, 'query': query})
