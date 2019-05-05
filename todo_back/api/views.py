import json
from django.http import HttpResponse, JsonResponse
from api.models import TaskList, Task


# Create your views here.

def index(request):
    return HttpResponse('<h1>Index page</h1>')


def about(request):
    return HttpResponse('<h1>About page</h1>')


