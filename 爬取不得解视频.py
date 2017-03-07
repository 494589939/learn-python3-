#! /usr/bin/env python
from bs4 import BeautifulSoup
import requests,urllib


#解析URL
def req(url):
    try:
        headers={"User-Agent":"Mozilla/5.0"}
        html=requests.get(url,headers=headers)
        html.raise_for_status()
        html.encoding=html.apparent_encoding
        soup=BeautifulSoup(html.text,"html.parser")
        return soup
    except:
        print("输入错误")
#获取视频URL地址并下载
def filt(soup):
    for names in soup.select(".j-video-c"):#筛选名字
        for video in names.select(".j-video"):#筛选URL
            name=names.get("data-title")[:-3]
            mp=video.get("data-mp4")
            urllib.request.urlretrieve(mp,r'D:\python项目\video\%s.mp4'%name)
            print("正在下载："+name+mp)


if __name__=="__main__":
    page=input("请输入要结束的页数：")
    i=1
    while i <=int(page):
        url="http://www.budejie.com/video/%s"%i
        filt(req(url))
        i+=1





