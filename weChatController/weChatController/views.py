import json
from .operator import send_message
from django.shortcuts import render, HttpResponse


def home_page(request):
    return render(request, 'index.html')


def submit(request, msg):
    print(msg)
    send_message(msg)
    return HttpResponse(json.dumps(dict(
        raw=str(request.path),
        state='success'
    )))
