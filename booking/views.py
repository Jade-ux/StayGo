from django.shortcuts import render

def booking(request):
    """This view returns the booking form page"""

    return render(request, 'booking/booking.html')
    