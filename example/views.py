# example/views.py
from datetime import datetime

from django.http import HttpResponse

import json

import httpx
@csrf_exempt
def index(request):
    now = datetime.now()
    if request.method!="POST":
        return HttpResponse("Sorry, only POST is supported. If you are a regular user looking at this page, no worries! Just close this page and continue on!")
    res={}
    res["success"]=True
    res["body"]=httpx.get("https://google.com").text
    return HttpResponse(json.dumps(res, sort_keys=True, indent=2))
