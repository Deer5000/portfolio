from django.http import HttpResponse
# from django.template import loader



def home(request):
    return HttpResponse("Portfolio Home")

def contact(request):
    return HttpResponse("Contact Me")
