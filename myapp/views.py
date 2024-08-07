from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

from .models import Profile


# def index(request):
#     return HttpResponse("Hello, world. You're at the polls index.")

def profile_view(request):
    profile = Profile.objects.first()  # Assuming only one profile exists
    return render(request, 'profile.html', {'profile': profile})