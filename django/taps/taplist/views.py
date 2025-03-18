from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseBadRequest
from .models import beer

# RSS Feed
import feedparser
import sys, codecs
sys.stdout = codecs.getwriter('utf-8')(sys.stdout)
from django.core.mail import (send_mail, BadHeaderError,)

# Create your views here.
def index(request):
	beers = beer.objects.filter(kegged = 'True')
	# Brewery Link
	url = 'https://untappd.com/rss/brewery/367780'
	feeder = feedparser.parse(url)
	for entry in feeder['entries']:
		title = entry['title']
		link = entry['link']
		pubDate = entry['published']
		pubparsed = entry['published_parsed']
		context = {
			'title':title,
			'link':link,
			'pubDate':pubDate,
			'pubparsed':pubparsed,
		}

	return render(request, 'taplist.html', {'beer': beers, 'context': context})
	#return HttpResponse("Hello, world. You're at the polls index.")