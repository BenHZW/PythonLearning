from django.shortcuts import render
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse,Http404
from searcher.models import New

import subprocess
import threading

import json

import requests
import re
import json
import time
from bs4 import BeautifulSoup
import pymysql



def index(request):
    return render(request, 'searcher/index.html')


def detail(request):

    artid = request.GET.get("artid")
    new = New.objects.filter(artid__icontains=artid).first()
    return render(request, 'searcher/result.html', {'new': new})

def list(request):
    arttype = request.GET.get("arttype")
    if arttype:
        news = New.objects.filter(arttype__icontains=arttype)[:10]
    else:
        news = New.objects.all()[:10]
    return render(request, 'searcher/list.html', {'news': news})

@csrf_exempt
def search(request):
    data = {
        "success": True,
        "data": {}
    }

    if request.method == "POST":
        keyword = request.POST.get("keyword")
        arttype = request.POST.get("arttype")
        print(keyword,arttype)
        if keyword == "":
            data['lenght'] = 0
            return HttpResponse(json.dumps(data), content_type="application/json")
        else:
            if arttype == "全部":
                news = New.objects.filter(title__icontains=keyword)
            else:
                news = New.objects.filter(title__icontains=keyword, arttype__icontains=arttype)
            data['lenght'] = len(news)
            data['data']["result"] = json.loads(serializers.serialize("json", news))
            return HttpResponse(json.dumps(data), content_type="application/json")

    return Http404



@csrf_exempt
def start(request):
    if request.method == "POST":
        # prints = PrintThread()
        # prints.start()
        # prints.join()

        db = pymysql.connect("localhost", "root", "root", "news")
        cursor = db.cursor()


        cursor.close()
        db.close()

        return HttpResponse("over!")
    return render(request, 'searcher/start.html')

# 爬取线程
class PrintThread(threading.Thread):
    def run(self):
        cmd = r"C:\Users\Administrator\AppData\Local\Programs\Python\Python36-32\python.exe C:\Users\Administrator\Desktop\code\网站代码\mysite\searcher\spider.py"
        s = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
        s.wait()