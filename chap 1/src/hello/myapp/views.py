# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def view1(request):
	return HttpResponse("<h1>hello world</h1>")
