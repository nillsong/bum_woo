from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
#def send(receiveEmail, verifyCode):
def send(reqest):
    return HttpResponse("sendEmail, send function")
