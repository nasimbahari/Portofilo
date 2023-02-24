from django.shortcuts import render
from .models import educations
# Create your views here.
def index(request):
    educ=educations.objects
    return render(request,'educations/index.html', {"educ":educ})