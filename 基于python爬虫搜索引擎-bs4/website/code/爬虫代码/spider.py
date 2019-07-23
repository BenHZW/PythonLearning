import requests
import re

import time
from bs4 import BeautifulSoup
import pymysql

headers = {
    "Cookie":"JSESSIONID=E911521FA51B873312D5DAD47558F7B0; JSESSIONID=A3A020D7F11F2BB82847ECC0062F3FF5",
    "User-Agent":"Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36",
    "x-requested-with":"XMLHttpRequest",
    "Content-Type":"application/x-www-form-urlencoded",
}

reqNum = 0

req = requests.session()
req.headers = headers

db = pymysql.connect("localhost", "root", "cao518518", "allData")
cursor = db.cursor()

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
def loadPage(url):
    global req
    global reqNum
    reqNum +=1
    print("程序第",reqNum,"次请求~")
    try:
        response = req.get(url,timeout=10)
    except:
        response = req.get(url, timeout=10)
    html = response.content.decode("utf-8")
    # print(html)
    if html=="":
        time.sleep(15)
        try:
            response = req.get(url, timeout=10)
        except:
            response = req.get(url, timeout=10)
        html = response.content.decode("utf-8")
        # raise (Exception("服务器不给数据,请重置起始页后重启！"))

    if "Access to this page has been denied because we believe you are using automation tools to browse the website." in html:
        print("err-被检查")
        print("url",url)
        time.sleep(60*15)
        raise Exception("错误重启。")
        req = requests.session()
        req.headers = headers
    return html
@log("execute")

def crawlIndex(cursor):
    newsTypeList = [
        "学术顾问", "讲座教授", "教育部新世纪优秀人才", "广东省南粤优秀教师", "校报", "学校要闻", "校园动态", "通知公告","招投标",
        "高教动态","媒体南方","学术讲座"
    ]

    typeDict = {
        "学术顾问": "http://www.nfsysu.cn/index.php/home/article/index/cid/130.html",
        "讲座教授": "http://www.nfsysu.cn/index.php/home/article/index/cid/131.html",
        "教育部新世纪优秀人才": "http://www.nfsysu.cn/index.php/home/article/index/cid/132.html",
        "广东省南粤优秀教师": "http://www.nfsysu.cn/index.php/home/article/index/cid/133.html",
        "校报": "http://www.nfsysu.cn/index.php/home/article/index/cid/51.html",
        "学校要闻": "http://www.nfsysu.cn/index.php/home/article/index/cid/15.html",
        "校园动态": "http://www.nfsysu.cn/index.php/home/article/index/cid/16.html",
        "通知公告": "http://www.nfsysu.cn/index.php/home/article/index/cid/17.html",
        "招投标": "http://www.nfsysu.cn/index.php/home/article/index/cid/26.html",
        "高教动态": "http://www.nfsysu.cn/index.php/home/article/index/cid/18.html",
        "媒体南方": "http://www.nfsysu.cn/index.php/home/article/index/cid/19.html",
        "学术讲座": "http://www.nfsysu.cn/index.php/home/article/index/cid/25.html",
    }

    for newsType in newsTypeList:
        page = 1
        while True:
            url = typeDict[newsType].replace(".html","/p/"+str(page)+".html")

            html = loadPage(url)
            if "资料正在整理中..." in html:
                break

            titleTagSearch = re.compile('<div class="news_title"><a href="/index.php/home/article/detail/cid/(.*?)/id/(.*?).html" title="(.*?)">').findall(html)

            for cid,artId,title in titleTagSearch:
                link = "http://www.nfsysu.cn/index.php/home/article/detail/cid/"+cid+"/id/"+artId+".html"

                crawlDetail(cid,artId,link,title,newsType)

            page += 1

def crawlDetail(cid,artId,url,title,newsType):
    html = loadPage(url).replace("/Public/Uploads/images/","http://www.nfsysu.cn/Public/Uploads/images/")
    soup = BeautifulSoup(html,"html.parser")
    pubTimeTag = soup.find("p",attrs={'class':'detail-time'})
    pubtime = ""
    if pubTimeTag:
        pubtime = pubTimeTag.get_text()
    contentTag = soup.find("div",attrs={'class':'ny_content'})
    if contentTag:
        content = str(contentTag).replace('<div class="ny_content">',"").strip("</div>")
        sql = """INSERT INTO news(artid,title,url,pubtime,content,detailcontent,arttype)
                                         VALUES ('%s','%s', '%s', '%s','%s','%s', '%s')""" % (
        artId, title, url, pubtime, cid, content, newsType)
        print("正在爬取",url)
        try:
            # 执行sql语句
            cursor.execute(sql)
            # 提交到数据库执行
            db.commit()
        except Exception as e:
            print(e)
            print("此条数据插入有误！")
            # 如果发生错误则回滚
            db.rollback()



if __name__ == '__main__':


    crawlIndex(cursor)
    cursor.close()
    db.close()