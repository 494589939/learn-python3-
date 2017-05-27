# encoding="utf-8"
# !/usr/bin/python
from bs4 import BeautifulSoup
from selenium import webdriver
import time
import pymssql

# 保存到SQL_Server数据库内
def saveSQL(text):
    conn = pymssql.connect(server='127.0.0.1', user='sa', password='a68503060', database="HelloWorld", charset="UTF-8")
    cursor = conn.cursor()
    cursor.executemany(
        "INSERT INTO xc_spider VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
        [text])
    # # 可以在不删除表的情况下删除所有的行
    # cursor.execute("DELETE FROM xc_spider;")
    conn.commit()

# 开启webdirver的PhantomJS浏览器用来解析对象，注意路径配置
driver = webdriver.PhantomJS()
# 之后可以定制URL
URL = 'http://flights.ctrip.com/booking/WNZ-BJS-day-1.html?DDate1=2017-05-30'
# GET方法获取相关源代码
driver.get(URL)
# 手动设置延迟规避封锁给网页充分的加载时间,后期可以做个IP池。
time.sleep(10)
# 用selenium的webdriver方法调用page_source函数在传入BeautifulSoup中
bs = BeautifulSoup(driver.page_source, 'html.parser')
for file in bs.select('.J_header_row'):
    for logo in file.select(".J_flight_no"):
        planeName = logo.get("data-flight")             # 航班号
        logoName = logo.select('.flight_logo')[0].text  # 航班对应的公司
        if len(logo) > 4:                               # 根据字符长度判断是否为共享航班
            share = "共  享:" + logo.select('.shared_flight')[0].get('data-content')
        else:
            share = "非共享"
        planeLow = file.select('.logo > .low_text')[0].text  # 确定飞机型号
        # 对出发时间和出发地点进行筛选 并且进行切片便于存入数据库
        right_local = file.select('.right')[0].text
        leaveTime = right_local[0:5]     # 出发时间
        leaveStation = right_local[5:]   # 出发地点
        # 对到达时间和到达地点进行筛选 并且进行切片便于存入数据库
        left_local = file.select('.left')[0].text
        reachTime = left_local[0:5]      # 到达时间
        reachStation = left_local[5:]    # 到达地点
        zdl = file.select('.service-item')[0].text  # 准点率，可切片截取
        price = file.select('.price ')[0].text      # 价格￥，可切片截取
        #       航班号     航空公司    机型   是否共享 出发时间   出发地点      到达时间   到达地点   准点率  价格
        text = (planeName, logoName, planeLow, share, leaveTime, leaveStation, reachTime, reachStation, zdl, price)
        # 准备保存到数据库
        print(text)
        saveSQL(text)
        print("保存成功")
driver.quit()


