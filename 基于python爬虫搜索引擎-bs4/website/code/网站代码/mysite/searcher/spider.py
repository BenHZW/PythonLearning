import requests
import re
import json
import time
from bs4 import BeautifulSoup
import pymysql

db = pymysql.connect("localhost", "root", "root", "news")
cursor = db.cursor()

headers = {
    "Cookie":"cnsuuid=1bf5f905-e92f-7f41-185a-8473717e8e0e3710.1410744528885_1547614437659; Hm_lvt_0da10fbf73cda14a786cd75b91f6beab=1547614439; __jsluid=83bd89f4c9f897f3db4ee9b62a2a6399; Hm_lpvt_0da10fbf73cda14a786cd75b91f6beab=1547614921",
    "User-Agent":"Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36",
}

req = requests.session()
req.headers = headers
reqNum = 0

def retry(count=1):
    def dec(f):
        def ff(*args, **kwargs):
            ex = None
            for i in range(count):
                try:
                    ans = f(*args, **kwargs)
                    return ans
                except Exception as e:
                    ex = e
            raise ex

        return ff

    return dec


def log(text):
    def decorator(func):
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)

        return wrapper

    return decorator


@retry(3)
def loadPage(url,encoding=None):
    global reqNum
    reqNum +=1
    print("程序第",reqNum,"次请求~")
    try:
        response = req.get(url,timeout=10)
    except:
        response = req.get(url, timeout=10)
    if encoding:
        try:
            html = response.content.decode(encoding,"ignore")
            return html
        except:pass
    html = response.content.decode(response.encoding)

    # print(html)
    # if "403" and "黑客" in html:
    #     print("err-被检查")
    #     print("url",url)
    #     time.sleep(60*15)
    #     raise Exception("错误重启。")
    #     req = requests.session()
    #     req.headers = headers
    return html
@log("execute ==>> ")
def crawlSimple(newsTypeList = ["时政","社会","国际","财经", "体育","产经","台湾","金融"],maxPage = 2,pageNum = 30):

    nowTime = lambda: int(round(time.time() * 1000))

    typeDict = {
        "时政":"http://channel.chinanews.com/cns/cjs/gn.shtml",
        "社会":"http://channel.chinanews.com/cns/cjs/sh.shtml",
        "国际":"http://channel.chinanews.com/cns/cjs/gj.shtml",
        "财经":"http://channel.chinanews.com/cns/cjs/cj.shtml",
        "体育":"http://channel.chinanews.com/cns/cjs/ty.shtml",
        "产经":"http://channel.chinanews.com/cns/cjs/business.shtml",
        "台湾":"http://channel.chinanews.com/cns/cjs/tw.shtml",
        "金融":"http://channel.chinanews.com/cns/cjs/fortune.shtml",
    }

    for newsType in newsTypeList:
        for page in range(1,maxPage+1):
            curUrl = typeDict[newsType]+"?pager={}&pagenum={}&_={}".format(page,pageNum,nowTime)
            html = loadPage(curUrl)
            jsonData = json.loads(html.replace("var specialcnsdata = ",""))
            for dataItem in jsonData['docs']:
                aid = dataItem['id']
                title = dataItem['title']
                url = dataItem['url']
                pubtime = dataItem['pubtime']
                content = dataItem['content']
                print("-----------------------")
                print("type",newsType)
                print("id",aid)
                print("title",title)
                print("url",url)
                print("pubtime",pubtime)
                print("content",content)
                detailContent = crawlDetail(url)
                sql = """INSERT INTO news(artid,title,url,pubtime,content,detailcontent,arttype)
                                 VALUES ('%s','%s', '%s', '%s','%s','%s', '%s')""" % (aid, title,url,pubtime,content,detailContent,newsType)
                try:
                    # 执行sql语句
                    cursor.execute(sql)
                    # 提交到数据库执行
                    db.commit()
                except:
                    print("此条数据插入有误！")
                    # 如果发生错误则回滚
                    db.rollback()


def crawlDetail(url):
    html = loadPage(url,"gb2312")
    soup = BeautifulSoup(html,"html.parser")
    articleTag = soup.find("div",attrs={'class':'left_zw'})
    if articleTag:
        article = str(articleTag).replace('<div class="left_zw" style="position:relative">',"").replace('</p></div>',"")
        print("article ok!")
        return article
    return None





if __name__ == "__main__":
    crawlSimple()
    cursor.close()
    db.close()

