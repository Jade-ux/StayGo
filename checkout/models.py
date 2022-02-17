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
    number_of_people = models.IntegerField(null=False, default=0)
    number_of_days = models.IntegerField(null=False, default=0)
    # Edit options
    date_range = models.CharField(max_length=100, null=True, blank=True)
    date_from = models.DateTimeField(editable=True)
    date_to = models.DateTimeField(editable=True)
    total = models.DecimalField(max_digits=6, decimal_places=2, null=False, default=0)
    deposit = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)
    total_paid = models.DecimalField(max_digits=6, decimal_places=2, null=False, default=0)
    total_due = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)
    # original_cart = models.TextField(null=False, blank=False, default='')
    stripe_pid = models.CharField(max_length=254, null=False, blank=False, default='')

    def _generate_order_number(self):
        """
        Generate a random, unique order number using UUID
        """
        return uuid.uuid4().hex.upper()

    #
    #def update_total_due(self): 
        """
        Updates the total due when customer pays the deposit and balance
        """
        # self.total_due = self.grand_total.aggregate(Sum(''))