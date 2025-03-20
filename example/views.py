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
        templ={
            "url": str,
            "method": str,
            "headers": dict,
            "body": (str)
        }
        for key, expected_type in required_keys.items():
            if key not in data:
                raise ValueError(f"Missing required key: {key}")
            if not isinstance(data[key], expected_type):
                raise TypeError(f"Invalid type for {key}: Expected {expected_type}, got {type(data[key])}")
        res["success"]=True
        req=httpx.get("https://google.com")
        res["body"]=base64.b64encode(req.content).decode('utf-8')
        res["headers"]=dict(req.headers)
        res["status"]=req.status_code
        rsp=HttpResponse(json.dumps(res),content_type="application/json")
        return rsp
    except BaseException as e:
        return HttpResponse(f"Internal error! Error message: {e}",status=500)
