import requests
import time
import random
import traceback
from xlwt import *
from bs4 import BeautifulSoup

# 获取请求内容
def get_urls(url, headers):
    try:
        r = requests.get(url, headers=headers)
        r.raise_for_status()
        r.encoding = "utf-8"
        return r.text
    except:
        print(" ")

# 解析网页内容
def get_file(html, find_keys, new_list):
    soup = BeautifulSoup(html, "lxml")
    files = soup.select("div#content_left")[0]
    try:
        for i in range(10):
            link = files.select("h3 > a:nth-of-type(1)")[i].get("href")
            totle = files.select('h3 > a')[i].text
            # 关键字筛选
            for word in find_keys:
                if word in totle:
                    wjxx = [totle, link]
                    # 建个列表去除重复URL链接
                    if wjxx not in new_list:
                        new_list.append(wjxx)
        # 添加延迟模拟人类操作，防止被封
        times = random.uniform(0.8, 2)
        time.sleep(times)
        return new_list
    except:
        print(' ')

def excel_list(key,news_list):
    w = Workbook(encoding='utf-8')
    wb = w.add_sheet(key, cell_overwrite_ok=True)
    header = ['政策标题', '政策URL链接']
    for i in range(2):
        wb.write(0, i, header[i], easyxf('font: bold on'))
    # 开始写入数据
    index = 1
    # 遍历需要写入的文件列表
    for List in news_list:
        # 当 j 在需要写入的列表的内容长度内进行遍历
        for j in range(len(List)):
            #     # 开始写入内容的行和列
            wb.write(index, j, List[j])
        # 注意此处缩进
        index += 1
        w.save(key+'.xls')

if __name__ == '__main__':
    new_list = []
    # key = '浙江省千人计划'
    # find_key = ["补助", "方法", "办法", "暂行", "管理"]
    key = '物联网智慧城市'
    find_key = [ '架构', '补助']

    start_page = 1
    end_pages = 20
    for page in range((start_page-1)*10, end_pages*10, 10):
        url = "https://www.baidu.com/s?wd={0}&pn={1}".format(key, page)
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
               'Accept':'text/html;q=0.9,*/*;q=0.8',
               'Accept-Charset':'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
               'Accept-Encoding':'gzip',
               'Connection': 'close',
               'Referer': None
                # 注意如果依然不能抓取的话，这里可以设置抓取网站的host
                }
        html = get_urls(url, headers)
        get_file(html, find_key, new_list)
    excel_list(key, new_list)
    print('保存完成')


