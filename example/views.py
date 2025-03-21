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
        #if request.method!="POST":
        #    r=HttpResponse(f"Sorry, only POST is supported. If you are a regular user looking at this page, no worries! Just close this page and continue on!",status=500)
        #    r["Access-Control-Allow-Origin"] = "*"
        #    return r
        res={}
        templ={
            "url": str,
            "method": str,
            "headers": dict,
            "body": (str)
        }
        #jsn=json.loads(request.body.decode('utf-8'))
        #for key, expected_type in templ.items():
        #    if key not in jsn:
        #        raise ValueError(f"Missing required key: {key}")
        #    if not isinstance(jsn[key], expected_type):
        #        raise TypeError(f"Invalid type for {key}: Expected {expected_type}, got {type(jsn[key])}")
        #res["success"]=True
        req=0
        if request.method in ["POST", "PUT", "PATCH", "DELETE", "OPTIONS", "TRACE"]:
            req=httpx.request(request.method,"https://"+request.path[1:],headers=dict(request.headers),data=request.body.decode())
        else:
            req=httpx.request(request.method,"https://"+request.path[1:],headers=dict(request.headers))
        #res["body"]=base64.b64encode(req.content).decode('utf-8')
        #res["headers"]=dict(req.headers)
        #res["status"]=req.status_code
        rsp=0
        if "content-type" in req.headers:
            rsp=HttpResponse(bytes(str(dict(request.headers)),encoding="utf-8")+bytes("<h1>https://"+request.path[1:]+"</h1>",encoding="utf-8")+req.content,content_type=req.headers["content-type"])
        else:
            rsp=HttpResponse(bytes(str(dict(request.headers)),encoding="utf-8")+bytes("<h1>https://"+request.path[1:]+"</h1>",encoding="utf-8")+req.content)
        rsp["Access-Control-Allow-Origin"] = "*"  # Allow any origin to access this resource
        rsp["Access-Control-Allow-Methods"] = "*"  # Allow specific methods
        rsp["Access-Control-Allow-Headers"] = "*"  # Allow specific headers
        return rsp
    except BaseException as e:
        r=HttpResponse(f"Internal error! Error message: {e}",status=500)
        r["Access-Control-Allow-Origin"] = "*"
        return r
