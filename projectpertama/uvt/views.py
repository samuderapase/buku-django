from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect, HttpResponse


def home(request):
    return render_to_response ('base.html')
