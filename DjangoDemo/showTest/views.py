from django.http import HttpResponse

# Create your views here.

def hello(request):
    return HttpResponse("这是一个django页面")