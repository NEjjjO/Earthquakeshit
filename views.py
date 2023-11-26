# views.py
from django.shortcuts import render, redirect
from .forms import EventForm
from .models import Event

def add_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            event = Event(
                start_time=form.cleaned_data['start_time'],
                end_time=form.cleaned_data['end_time'],
                magnitude=form.cleaned_data['magnitude'],
                depth=form.cleaned_data['depth'],
                latitude=form.cleaned_data['latitude'],
                longitude=form.cleaned_data['longitude'],
            )
            event.save()
            return redirect('success')  # Redirect to a success page
    else:
        form = EventForm()

    return render(request, 'add_event.html', {'form': form})
