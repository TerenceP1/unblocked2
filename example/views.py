# example/views.py
from datetime import datetime

from django.http import HttpResponse

def index(request):
    now = datetime.now()
    if request.method!="POST":
        return HttpResponse("Sorry, only POST is supported. If you are a regular user looking at this page, no worries! Just close this page and continue on!")
    html = f'''
    <html>
        <body>
            <h1>Hello from Vercel!</h1>
            <p>The current time is { now }.</p>
        </body>
    </html>
    '''
    return HttpResponse(html)
