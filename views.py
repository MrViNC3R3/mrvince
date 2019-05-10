from django.http import HttpResponse
from django import get_version

source = 'https://github.com/zeit/now-examples/tree/master/python-django'
css = '<link rel="stylesheet" href="/css/style.css" />'

def index(request):
    return HttpResponse("%s<h1 style='text-align:center;'>Welcome !</h1><p>" % (css), content_type='text/html')
