import requests
from bs4 import BeautifulSoup
# 获取源代码的文本格式
def get_html(url):
    try:
        headers = {"User-Agent": "Mozilla/5.0 (compatible; Baiduspider/2.0; +http://www.baidu.com/search/spider.html)"}
        r = requests.get(url, headers=headers)
        r.raise_for_status()
        # r.apparent_encoding
        r.encoding = "utf-8"
        return r.text
    except requests.HTTPError as e:
        return "出现错误！", e

# BS4解析出符合关键字的 标题 时间与URL连接
def find_file(html,keys):
    file = BeautifulSoup(html, "lxml")
    news_list = []
    for i in range(15):
        file_time = file.find_all(style="color: #626262")[i].text.replace('\n', '')
        file_name = file.select(".lyh1 > a")[i].get("title")
        page_url = file.select(".lyh1 > a")[i].get("href")
        file_url = "http://www.zjkjt.gov.cn" + page_url
        for key in keys:
            if key in file_name:
                wjxx = [file_name, file_time, file_url]
                # 建个列表去除重复URL链接
                if wjxx not in news_list:
                    news_list.append(wjxx)
    for file in news_list:
        print(file)
        with open("D:\python-file\通告信息.txt", "a+") as f:
                f.write(str(file)+"\n\n")

# 主程序框架
if __name__ == '__main__':
    pages = int(input("请输入要爬取的页数（例如 14 ）："))
    # 以下关键字请勿重复
    # pages = 1
    key_words = ["申", "计划", "奖", "重点", "组织", "资金", "扶持"]
    for page in range(1, pages+1):
        url = "http://www.zjkjt.gov.cn/html/node01/list0101/0101_{}.html".format(page)
        html = get_html(url)
        find_file(html, key_words)
    # print(files)