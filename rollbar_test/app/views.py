from django.shortcuts import render
from django.http import HttpResponse   
import rollbar
import sys



def info(request):
    rollbar.report_message('the index was requested', 'info',request)
    return HttpResponse("Hello, world. You're at the index.")

def error(request):
    try:
        2019 / 0
    except:
        rollbar.report_exc_info(sys.exc_info(), request)
        raise

def warning(request):
    rollbar.report_message('WARNING: Bad men here!!!  ', 'warning',request)
    return HttpResponse("Hello, world. You're at the warning.")

def critical(request):
    rollbar.report_message('An critical error occured!  ', 'critical',request)
    return HttpResponse("Hello, world. You're at the critical.")


