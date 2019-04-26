from django.http import HttpResponse


def index(request):
    return HttpResponse("Hi, world. You're at the lol index.")