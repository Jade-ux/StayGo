import uuid

from django.db import models
from django.db.models import Sum
from django.conf import settings

from django_countries.fields import CountryField

from vans.models import Van

class BookingOrder(models.Model):
    booking_number = models.CharField(max_length=32, null=False, editable=False)
    van = models.ForeignKey(Van, null=False, blank=False, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    country = CountryField(blank_label='Country *', null=False, blank=False)
    postcode = models.CharField(max_length=20, null=True, blank=True)
    town_or_city = models.CharField(max_length=40, null=False, blank=False)
    street_address1 = models.CharField(max_length=80, null=False, blank=False)
    street_address2 = models.CharField(max_length=80, null=True, blank=True)
    county = models.CharField(max_length=80, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    # Booking details
    destination = models.EmailField(max_length=254, null=False, blank=False)
    number_of_people = models.IntegerField(max_digits=3, null=False, default=0)
    number_of_days = models.IntegerField(max_digits=6, null=False, default=0)
    # Edit options
    date_from = models.DateTimeField(auto_now_add=True)
    date_to = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=6, decimal_places=2, null=False, default=0)
    deposit = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)
    total_paid = models.DecimalField(max_digits=6, decimal_places=2, null=False, default=0)
    total_due = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)
    # original_cart = models.TextField(null=False, blank=False, default='')
    stripe_pid = models.CharField(max_length=254, null=False, blank=False, default='')
