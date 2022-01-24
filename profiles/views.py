from django.shortcuts import render


def profiles(request):
    """This view returns the profiles page"""

    return render(request, 'profiles/profiles.html')
