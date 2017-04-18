import requests
from bs4 import BeautifulSoup
# 获取源代码的文本格式
def get_html(url):
    try:
        headers = {"User-Agent": "Mozilla/5.0 (compatible; Baiduspider/2.0; +http://www.baidu.com/search/spider.html)"}
        r = requests.get(url, headers=headers)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except requests.HTTPError as e:
        return "出现错误！", e

def find_file(html, keys):
    file = BeautifulSoup(html, "lxml")
    a = file.select(".ny-list > #3979414 ")#[0].text
    print(type(a))
    print(a)
    print(a.find_all("a"))



# 主程序框架
if __name__ == '__main__':
    pages = int(input("请输入要爬取的页数（例如 14 ）："))
    # 以下关键字请勿重复
    # pages = 1
    key_words = ["申", "计划", "奖", "组织", "资金", "扶持"]
    for page in range(1, pages+1):
        url = "http://wzjxw.wenzhou.gov.cn/col/col1210255/index.html?uid=3979414&pageNum={}.html".format(page)
        html = get_html(url)
        files = find_file(html, key_words)