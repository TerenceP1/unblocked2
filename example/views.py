# example/views.py
from datetime import datetime

from django.http import HttpResponse

import json

import httpx
import base64
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def index(request):
    try:
        now = datetime.now()
        if request.method!="POST":
            return HttpResponse("Sorry, only POST is supported. If you are a regular user looking at this page, no worries! Just close this page and continue on!")
        res={}
        res["success"]=True
        req=httpx.get("https://google.com")
        res["body"]=base64.b64encode(req.content).decode('utf-8')
        res["headers"]=req.headers
        req["status"]=req.status_code
        rsp=HttpResponse(json.dumps(res))
        return rsp
    except BaseException as e:
        return HttpResponse(f"Internal error! Error message:{e}")
