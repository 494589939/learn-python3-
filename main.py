import requests
import time
import random
import hashlib
import json
from tkinter import Tk, Button, Label, Text, Menu, Entry, END



# 创建一个爬取有道的结果爬虫类获取结果
class YouDaoHelp(object):
    def __init__(self):
        pass

    # 爬取结果答案
    def crawl(self,content):
        # 通过分析JS文件获得2个盐加密的解决办法
        # 1. 时间戳，因为JS都是毫秒 要乘以 1000
        timestamp=int(time.time()*1000)+random.randint(0,10)

        # 2.sign 文件 md5解码
        t=content
        i=str(timestamp)
        sign=hashlib.md5(("fanyideskweb"+t+i+"ebSeFb%=XZ%T[KZ)c(sy!").encode('utf-8')).hexdigest()

        data={
            'action': 'FY_BY_CLICKBU',
            'client': 'fanyideskweb',
            'doctype': 'json',
            'from': 'AUTO',
            'i': t,
            'keyfrom': 'fanyi.web',
            'salt': timestamp,
            'sign': sign,
            'smartresult': 'dict',
            'to': 'AUTO',
            'typoResult': 'false',
            'version': '2.1'
        }

        # 去掉url 的‘_o’ 部分能解决 50报错问题
        url='http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'
        try:
            r_str=requests.post(url,data=data,timeout=3)
            r_dict=json.loads(r_str.text)
            answer=r_dict['translateResult'][0][0]['tgt']
            # return answer
        except Exception as e:
            answer =('出现错误请确认网络已经链接：', e)
        finally:
            return answer
        

# 利用TK组件创建一个图形界面类，加强用户反馈
class Applicaltion(object):
    def __init__(self):
        # 将YouDaoHelp类引入
        self.helper=YouDaoHelp()

        # 下面开始创建图形框
        self.Windous=Tk()
        self.Windous.title('远or广翻译员')
        # geometry 初始化窗口大小 中间'x'连接  初始位置 用‘+’连接
        self.Windous.geometry('265x350+300+300')

        # 输入框 Entry 用于显示简单的文本内容
        # pack 包 ，grid 网格，place 位置 三种排序定位
        self.entry=Entry(self.Windous)
        self.entry.place(x=10,y=10,width=200,height=30)

        # 翻译按钮框Button
        self.submit_btn=Button(self.Windous,text='翻译',command=self.submit)
        # 如果点击输入的按钮是RErurn 
        self.submit_btn.bind_all("<Return>",self.key)
        # self.submit_btn.bind_all("<Key>",self.key)
        self.submit_btn.place(x=210,y=10,width=40,height=30)
        

        # 清空按钮框Button
        self.clean_btn=Button(self.Windous,text='清空',command=self.clean_entry)
        # self.clean_btn.bind_all("<DELETE>",self.key)
        self.clean_btn.place(x=210,y=45,width=40,height=30)

        # 翻译标题Label可以显示文本和位图
        self.title_label=Label(self.Windous,text='翻译结果如下所示:')
        self.title_label.place(x=10,y=50)

        # 文本展示框 Text用于显示多行文本
        self.result_text=Text(self.Windous,background='#ccc')
        self.result_text.place(x=10,y=80,width=240,height=250)

        # 初始化右键菜单区
        # tearoff = False ,代表将菜单项最上面的一条虚线去掉，默认是存在的
        self.menu=Menu(self.Windous,tearoff=False)
        # 定义右键菜单内容
        self.menu.add_command(label="复制（Copy）",command=self.entry_copy)
        self.menu.add_command(label="黏贴（Paste）",command=self.entry_paste)
        # 留空分割区
        self.menu.add_separator()
        self.menu.add_command(label="剪切（Cut）",command=self.entry_cut)
        # Windous绑定鼠标右键，可以操作的区域
        self.Windous.bind("<Button-3>",self.rightKey)

    # 右键菜单用到的函数
    def rightKey(self,event):
        self.menu.post(event.x_root,event.y_root)

    # 搜索框(entry)右键剪切功能
    def entry_cut(self,event=None):
        self.entry.event_generate("<<Cut>>")

    # 搜索框右键拷贝功能
    def entry_copy(self,event=None):
        self.entry.event_generate("<<Copy>>")

    # 搜索框的右键黏贴功能
    def entry_paste(self,event=None):
        self.entry.event_generate('<<Paste>>')

    # 绑定键盘 bind_all('<Return>',函数)  == ENTER
    def key(self,event=None):
        self.submit()

    # 清空按钮文本框
    def clean_entry(self):
        self.entry.delete(0,END)
    
    # 重点函数：获取输入的文本打印到下面的文本框,需要 导入END函数
    def submit(self):
        # 1.从输入框获取用户值
        content=self.entry.get()
        # 2.将值发送给有道
        result=self.helper.crawl(content)
        # 3.将结果显示在下面的文本框Text控件
        self.result_text.delete(1.0,END)
        self.result_text.insert(END,result)

    
    
    # 输入几秒后自动回车显示结果
    def Auto_enter(self):
        # self.submit()
        pass

    #  一直监听死循环
    def run(self):
        self.Windous.mainloop()


if __name__=='__main__':
    app=Applicaltion()
    app.run()
