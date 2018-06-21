from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Entry
from .forms import EntryForm

def index(request):
    if request.method == 'POST':
        form = EntryForm(request.POST or None)
        if form.is_valid():
            body = form.cleaned_data['body']
            new_entry = Entry(body=body)
            new_entry.save()
            entries = Entry.objects.all
            messages.success(request, ('Entry added to pad'))
            return render(request, 'index.html', {'entries': entries})
    
    entries = Entry.objects.all
    return render(request, 'index.html', {'entries': entries})

def delete(request, entry_id):
    entry = Entry.objects.get(pk=entry_id)
    entry.delete()
    messages.success(request, ('Entry removed from pad'))
    return redirect("index")

def archive_entry(request, entry_id):
    entry = Entry.objects.get(pk=entry_id)
    entry.archived = True
    entry.save()
    return redirect("index")

def unarchive_entry(request, entry_id):
    entry = Entry.objects.get(pk=entry_id)
    entry.archived = False
    entry.save()
    return redirect("index")

def archive(request):
    entries = Entry.objects.filter(archived=True)
    return render(request, 'index.html', {'entries': entries})
