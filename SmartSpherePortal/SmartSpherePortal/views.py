from django.http import HttpResponse, request

def home(request):
    return HttpResponse('portal home page')