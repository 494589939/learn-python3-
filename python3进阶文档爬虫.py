# # encoding="utf-8"
# #! /usr/bin/python
#
# import pymssql
#
# conn = pymssql.connect(server='127.0.0.1', user='sa', password='a68503060', database="HelloWorld", charset='UTF-8')
# cursor = conn.cursor()
# cursor.execute("select * from 总经办")
# # 筛选出一个
# # print(cursor.fetchone())
# # 筛选出全部
# print(cursor.fetchall())
# # INSERT
# # cursor.execute("INSERT INTO 总经办(id) VALUES (%s) ", 30)
# # DELETE
# # cursor.execute("DELETE FROM 总经办  WHERE 申请项目 IS NULL ")
# # 最后关闭
# conn.commit()

from selenium import webdriver
from bs4 import BeautifulSoup
import time

# 获得所有分页文章的URL和标题
def get_page():
    linkLists = []
    Start_url = 'http://docs.pythontab.com/interpy/'
    list_html = getHtml(Start_url)
    sp = BeautifulSoup(list_html, 'lxml')
    for link in sp.select('.toctree-l1 > a'):
        pages = link.get('href')
        url = 'http://docs.pythontab.com/interpy/' + pages
        # title = link.text
        linkLists.append(url)
    return linkLists

# 获取对应页面网页源代码
def getHtml(url):
    driver = webdriver.PhantomJS()
    driver.get(url)
    time.sleep(2)
    html = driver.page_source
    # 关闭浏览器驱动
    # driver.quit()
    return html

# 开始解析
def getText(html):
    sp = BeautifulSoup(html, 'lxml')
    text = sp.select('.section')[0].text
    return text

# 开始调用
def main():
    page_url = get_page()
    for page in page_url:  # 载入提取出每个分页的URL
        html = getHtml(page)  # 解析每个分页的URL
        text = getText(html)  # 提取出每个页面的内容
        print(text)


if __name__ == '__main__':
    main()

