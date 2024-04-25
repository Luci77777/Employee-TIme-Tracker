from django.shortcuts import render, redirect
from .models import TimeEntry
from .forms import TimeEntryForm

def time_entry_list(request):
    time_entries = TimeEntry.objects.all()
    return render(request, 'timetracker/time_entry_list.html', {'time_entries': time_entries})

def add_time_entry(request):
    if request.method == 'POST':
        form = TimeEntryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('time_entry_list')
    else:
        form = TimeEntryForm()
    return render(request, 'timetracker/add_time_entry.html', {'form': form})
