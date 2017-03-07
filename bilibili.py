import requests
from bs4 import BeautifulSoup
#分析URL
def req(url):
    try:
        html=requests.get(url)
        html.raise_for_status()
        html.encoding=html.apparent_encoding
        soup=BeautifulSoup(html.text,"lxml")
        return soup
    except:
        print("出现错误")

#bilibili拼接页码
def pages(soup,downloads):
    for filt in soup.select("option"):
        a=filt.get("value")# .split("/")[-1]#切片并提取最后一个页码进行拼接
        page=downloads+a
        name=filt.text
        dict[name]=page
        #print(page, name)
        #video(page,name) #返回拼接完成的URL
        with open(r"D:\python项目\tutorial\haha.txt","a+") as f:
            f.write(page+  name)

    #return dict
def video(page):#找到视频下载页码并拼接
    for i in page.keys():
        #print(i, page[i])
        for filt in req(page[i]).select(".Data_Mp4 .Data_Data a"):
            value=filt.get("href")
            if value !=None:
                #print(value)
                down_url=(downloads+filt.get("href"))
                print(req(down_url))
                break
                #for MP4 in req(down_url).select("display: block; a"):
                 #   print(MP4.get("href"))


dict={}
url = "http://www.bilibili.com/video/av8420181/"#用户提供的连接
downloads='http://www.jijidown.com'#哔哩哔哩下载连接
a=req(url)
b=pages(a,downloads)
print(b)