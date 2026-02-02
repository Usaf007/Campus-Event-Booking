from django.db import models
from django.contrib.auth.models import User  # We need the built-in User table

# 1. The Event Table
class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    location = models.CharField(max_length=100)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    total_seats = models.IntegerField()
    
    # NEW: The Image Field
    image = models.ImageField(upload_to='event_images/', blank=True, null=True)
    
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def seats_available(self):
        booked_count = self.booking_set.count() 
        return self.total_seats - booked_count

# 2. The Booking Table (The relationship between User and Event)
class Booking(models.Model):
    # ForeignKeys link tables together. 
    # If a User is deleted, their bookings are deleted (CASCADE).
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    
    # Store exactly when the booking happened
    booked_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.event.title}"