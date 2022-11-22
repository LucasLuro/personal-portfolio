from django.shortcuts import render
from .models import Certifications

def home(request):
    certifications = Certifications.objects.all()
    return render(request, "portfolio/home.html", {'certifications' : certifications})

def resume(request):
    return render(request, "portfolio/resume.html")