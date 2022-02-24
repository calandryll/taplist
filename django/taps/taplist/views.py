from django.shortcuts import render
from django.http import HttpResponse
from .models import beer

# Create your views here.
def index(request):
	beers = beer.objects.filter(kegged = 'True')
	return render(request, 'taplist.html', {'beer': beers})
	#return HttpResponse("Hello, world. You're at the polls index.")