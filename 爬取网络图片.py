import urllib.request
import re

def open_url(url):   #1--打开URL
    req=urllib.request.Request(url)
    req.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.75 Safari/537.36')
    page=urllib.request.urlopen(req)
    html=page.read().decode('GB2312')
    return html

def two_url(html):   #2-用正则匹配找出二级URL
    p = r"[^/']*\d+\d*\.shtml"
    imglist = re.findall(p,repr(html))
    split_url=list(set(imglist))#利用set集合的特性去除重复然后重新换回列表

    for each in split_url:
        new_urls = 'http://www.yaojingweiba.com/manhua/' + each
        #return new_urls

#def three_url(new_urls):#3-准备解析出的二级URLS找出最后的图片url
        html2 = open_url(new_urls)
        #print(html2)
        req = r"(http://img.[\S]*\b\b\.(jpe|png))"
        # req=re.compile(req)
        imglist = re.findall(req, repr(html2))
        #print(imglist)
        for each in imglist:
            imgurl=each[0]#元组中的第一个是URL
            img=str(imgurl)
            imgname = imgurl.split("/")[-1]#切片后获取文件名

            urllib.request.urlretrieve(img,imgname)
            print('妖尾'+imgname)



x=input('是否从最新集数自动爬取递减爬取请输入(Y/N)：')

if x == 'Y' or x == 'y':
    z=int(input('请输入开始的最新集数（如520：'))
    while True:
        url = 'http://www.yaojingweiba.com/manhua/fairytail%s.shtml' % z  # 一级url
        two_url(open_url(url))
        z -=1
else:
    while True:
        jishu=input('请输入要爬取的集数（例如521）：')
        url='http://www.yaojingweiba.com/manhua/fairytail%s.shtml'%jishu#一级url
        two_url(open_url(url))