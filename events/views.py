from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .models import Event, Booking

# 1. Homepage View
def home(request):
    events = Event.objects.all()
    return render(request, 'events/home.html', {'events': events})

# 2. Signup View
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

# 3. Booking Logic
@login_required
def book_event(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    
    # Check if already booked
    existing_booking = Booking.objects.filter(user=request.user, event=event).exists()
    
    if existing_booking:
        messages.warning(request, "You have already booked this event!")
        return redirect('home')

    # Check seats and book
    if event.seats_available() > 0:
        Booking.objects.create(user=request.user, event=event)
        messages.success(request, f"Success! You booked '{event.title}'.")
    else:
        messages.error(request, "Sorry, this event is fully booked.")

    return redirect('home')

# 4. My Bookings Dashboard
@login_required
def my_bookings(request):
    bookings = Booking.objects.filter(user=request.user).order_by('-booked_at')
    return render(request, 'events/my_bookings.html', {'bookings': bookings})

# 5. Cancel Booking Logic
@login_required
def cancel_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id, user=request.user)
    booking.delete()
    messages.success(request, "Booking cancelled successfully.")
    return redirect('my_bookings')