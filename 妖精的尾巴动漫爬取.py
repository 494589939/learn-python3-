#导入 来自 urllib 的 request 方法
import urllib.request

#基本爬虫代码 1.0

def starpng(s2,s3):#

    for i in range(1,20):
        if i <10:
            s3=i
        else:
            s2=''
            s3=i
        url = 'http://img.yaojingweiba.com/uploads/manhua/%s/%s%s.png' % (s1, s2, s3)
        urllib.request.urlretrieve(url, '妖尾%s-%s%s集.png' % (s1, s2, s3))
        print('正在爬取 妖尾%s-%s%s集.png' % (s1, s2, s3))

def starjpg(s2, s3):#出错后换.jpg格式搜索
    for i in range(1, 20):
        if i < 10:
            s3 = i
        else:
            s2 = ''
            s3 = i
        url = 'http://img.yaojingweiba.com/uploads/manhua/%s/%s%s.jpg' % (s1, s2, s3)
        urllib.request.urlretrieve(url, '妖尾%s-%s%s集.png' % (s1, s2, s3))
        print('正在爬取 妖尾%s-%s%s集.jpg' % (s1, s2, s3))

#主程序循环调用star(s2,s3)函数
s1=int(input('请输入要爬的最新集数：'))#把输入的字符串转换成整数
while True:
    try:#试错
        starpng(0,1)
        s1 -=1   #自动向上爬取上一集
    except:#出错后执行下面
        starjpg(0, 1)
        s1 -=1
