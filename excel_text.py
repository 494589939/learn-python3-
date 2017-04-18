from xlwt import *
import requests

def save_excel():
    w = Workbook(encoding='utf-8')
    wb = w.add_sheet('浙江省千人计划', cell_overwrite_ok=True)
    header = ['name', 'url链接']
    for i in range(2):
        wb.write(0, i, header[i], easyxf('font: bold on'))

    lists = [['1', '2'], ['22', '33']]
    index = 1
    # 遍历需要写入的文件列表
    for List in lists:
        # 当 j 在需要写入的列表的内容长度内进行遍历
        for j in range(len(List)):
        #     # 开始写入内容的行和列
            wb.write(index, j, List[j])
        #注意此处缩进
        index += 1
        w.save('text3.xls')



r = requests.get("http://blog.csdn.net/lihao21/article/details/51857385")
print(r.url)