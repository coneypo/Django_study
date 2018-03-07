from django.http import HttpResponse

# return strings
def hello_main(request):
    return HttpResponse("main_Hello world ! ")
def hello_test1(request):
    return HttpResponse("test1_Hello world ! ")
def hello_test2(request):
    return HttpResponse("test2_Hello world ! ")

from django.shortcuts import render

# return html
def hello(request):
    context={}
    context["hello"]="hello,world"
    return render(request, 'hello.html', context)
