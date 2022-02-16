from django.shortcuts import render, get_object_or_404
from datetime import datetime

from vans.models import Van


def booking(request):
    """This view returns the booking form page"""

    return render(request, 'booking/booking.html')


def add_to_cart(request, item_id):
    """Adds the van to the cart (booking)"""
    
    van = get_object_or_404(Van, pk=item_id)
    # This will return the date range as a string
    # In order to work with it I need it as a 
    date_range = request.POST.get('daterange')

    return render(request, 'booking/cart.html')
    