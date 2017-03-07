from tkinter import *
import tkinter.messagebox as messagebox
class Application(Frame):
    def __init__(self,master=None):
        Frame.__init__(self,master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.nameInput = Entry(self,text="这是一个小爬虫！")
        self.nameInput.pack()
        self.alertButton = Button(self,text="点我",command=self.hello)
        self.alertButton.pack()

    def hello(self):
        name = self.nameInput.get() or "world"
        messagebox.showinfo("Message","Hello, %s"%name)

#窗口界面
app = Application()
app.master.title("爬虫小窗口")
app.mainloop()
