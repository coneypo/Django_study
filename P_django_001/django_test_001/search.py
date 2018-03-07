from django.http import HttpResponse
from django.shortcuts import render_to_response

# form
def search_form(request):
    return render_to_response('search_form.html')

#def cnblogs_form(request):
 #   return render_to_response('cnblogs_TimeStamp.html')


# receive
def search(request):
    request.encoding='utf-8'
    if 'q' in request.GET:
        message = 'you search:'+request.GET['q']
    else:
        message = 'empty form'

    return HttpResponse(message)