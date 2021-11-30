from django.http import HttpResponse
from django.template import RequestContext
from django.template.response import TemplateResponse


def handler404(request, *args, **argv):


    return TemplateResponse(request, '404.html', {})


def handler500(request, *args, **argv):

    return TemplateResponse(request, '500.html', {})
