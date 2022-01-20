from django.shortcuts import render

def vans(request):
    """This view returns the vans page"""

    return render(request, 'vans/vans.html')
    