from django.shortcuts import (
    render, get_object_or_404, redirect)
from .models import Van

def vans(request):
    """This view returns the vans page"""

    vans = Van.objects.all()

    context = {
        'vans': vans,
    }

    # return render(request, 'vans/vans.html', context)
    return redirect(van_detail, van_id = 1)


def van_detail(request, van_id):
    """ A view to show individual product details """

    van = get_object_or_404(Van, pk=van_id)

    context = {
        'van': van,
    }

    return render(request, 'vans/van_detail.html', context)
