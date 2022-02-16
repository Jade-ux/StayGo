from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from vans.models import Van


# This makes this dictionary available to all apps across the site

def booking_details(request):

    booking_details = []
    number_of_days = 0
    deposit = 0
    total = 0
    total_paid = 0
    total_due = 0
    day_rate = 0

    total = day_rate * number_of_days
    deposit = total * Decimal(settings.BOOKING_DEPOSIT_PERCENTAGE / 100)
    total_due = total - total_paid

    context = {
        'booking_details': booking_details,
        'number_of_days': number_of_days,
        'deposit': deposit,
        'total': total,
        'total_paid': total_paid,
        'total_due': total_due,
    }

    return context


# Total will = day_rate * number_of_days - from van model day rate 
# Will need to add discounts for days - add to van model
# Need total_booking_fee and total_paid amounts in order to have a total_due amount - should this be in the booking (bag) or in checkout ()