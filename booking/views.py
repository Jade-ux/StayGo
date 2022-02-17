from datetime import datetime
from django.shortcuts import render, get_object_or_404,redirect


from vans.models import Van


def booking(request):
    """This view returns the booking form page"""

    return render(request, 'booking/booking.html')


def add_to_cart(request, item_id):
    """Adds the van to the cart (booking)"""
    
    van = get_object_or_404(Van, pk=item_id)
    # This will return the date range as a string
    date_range_str = request.POST.get('daterange')
    # This splits out the string into from and to dates and converts
    # into datetime format
    date_range_list = date_range_str.split(' - ')
    date_from_str = date_range_list[0]
    date_from = datetime.strptime(date_from_str, '%m/%d/%Y')
    date_to_str = date_range_list[1]
    date_to = datetime.strptime(date_to_str, '%m/%d/%Y')
    # Gets the session to store the cart info
    cart = request.session.get('cart', {})

    # Puts the van into the cart with the date from and date to
    # If the van exists in the cart already, it will be overwritten
    # with the new dates
    # cart[item_id] = (date_from.isoformat(), date_to.isoformat())

    # Updates the cart with the new details
    request.session['cart'] = cart

    # Takes user to Starsky booking form until there are more vans
    return render(request, 'booking/booking.html')
    