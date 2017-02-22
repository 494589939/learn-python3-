import requests
from bs4 import  BeautifulSoup

def TXT(url2):
    url = requests.get(url2)
    #print(url)
    url.encoding = ('utf-8')  # 确定编码
    soup = BeautifulSoup(url.text, 'html.parser')
    for news in soup.select('.main-text-wrap'):#找小说本体URL
        for names in news.select('.j_chapterName'):#获取标题
            name=names.text
        txts = news.select('.read-content')[0].text#获取正文
        print('开始下载%s'%name)

        with open('%s.txt'%(name), 'w') as f:
            f.write(name)#写入标题
            f.write(txts)#写入正文

#打开需要爬取的目录
s=input('输入需要爬取的小说主网址：')
url=s+'#Catalog'#拼接URL
html=requests.get(url)
soup=BeautifulSoup(html.text,'lxml')
urls=soup.select('div.volume li a')#可加a:nth-of-type(1) 表示直接提取a标签的第一个值
for new_url in urls:
    url='http:' +(new_url.get('href'))
    if len(url) >70:#加个判断筛选出非VIP的章节
        TXT(url)
    else:
        pass




