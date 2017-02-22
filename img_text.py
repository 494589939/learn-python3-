import urllib.request
import re
def getimg(page1):
    url = 'https://www.909df.com/pic/6/2017-02-18/193%s.html'%page1
    tou = urllib.request.Request(url)
    tou.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.75 Safari/537.36')
    html = urllib.request.urlopen(tou).read().decode('utf-8')
    #print(html)
    req=r'https://[\S]*\.jpg'
    img=re.findall(req,repr(html))

    for i in img:

        name=i.split('/')[-1]
        urllib.request.urlretrieve(i,'%s.jpg'%name)
        print(name)
try:
    for x in range(77,9980):
        getimg(x)
except :
    print ('ERROT')

