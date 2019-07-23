import requests
import re

url = "http://www.xiaoshuotxt.org/wuxia/1617/"
response = requests.get(url)
response.encoding = "utf-8"
html = response.text
print(html)
print("------------------")
title = re.findall(r'<meta name="keywords" content="(.*?),',html)[0]
print(title)

#持久化(写入txt)
fb = open('%s.txt'%title, 'w', encoding='utf-8')

#提取章节
menu = re.findall(r'正文(.*?)</table>',html)[0]
chapter_info_list = re.findall(r'<a href="(.*?)" title=".*?">(.*?)</a>',menu)
print(chapter_info_list)

#循环访问章节，并获取内容
for chapter_info in chapter_info_list:
    chapter_url = chapter_info[0]
    chapter_title = chapter_info[1]
    if 'http' not in chapter_url:
        chapter_url = 'http://www.xiaoshuotxt.org%s'%chapter_url
    else:
        pass
    chapter_response = requests.get(chapter_url)
    chapter_response.encoding = 'utf-8'
    chapter_html = chapter_response.text

#数据提取 (章)
    print(chapter_title)
    chapter_title = chapter_title.replace(' ', '')
    fb.write(chapter_title)
"""
#数据清洗（按页面规律）
    chapter_content = re.findall(r'<div class="panel-body" id="htmlContent">(.*?)</div>',chapter_html)
    chapter_content = chapter_content.replace(' ','')
    chapter_content = chapter_content.replace('<br /><br /><br>','')

#数据持久化（写入txt）,先要在前面新建文件
    fb.write(chapter_title)
    fb.write(' ')
    fb.write(chapter_content)
    fb.write(' ')

#用以下语句可以看到动态过程
    print(chapter_url)
"""