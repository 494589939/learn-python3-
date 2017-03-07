import requests

    #print(url.status_code)#返回HTTP的请求状态
    #print(url.text)#HTTP响应内容的字符串格式 即url的页面内容
    #print(url.encoding)#猜测响应的编码方式，注意此方法如果hrader中不存在charset就会默认显示ISO-8859-1
    #print(url.apparent_encoding)#从内容分析出编码方式（备选方式），此方法比上方法更准确的获得编码
    #print(url.content)#响应二进制形式
'''
try:
    urls='https://www.baidu.com/s'
    heads={"wd":"Python"}
    url=requests.get(urls,params=heads)
    print(url.request.url)
    url.raise_for_status()
    url.enconding=url.apparent_encoding
    print(url.text)
except:
    print( "出现错误")
'''
for i in range(0,2):
    print(type(str(i*44)))
