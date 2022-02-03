from django.shortcuts import render


def faqs(request):
    """This view returns the faqs page"""

    return render(request, 'faqs/faqs.html')
    