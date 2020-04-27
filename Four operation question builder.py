"""
能够自动生成四则运算练习题
可以定制题目数量
用户可以选择运算符
用户设置最大数（如十以内、百以内等）
用户选择是否有括号、是否有小数
用户选择输出方式（如输出到文件、打印机等）
最好能提供图形用户界面（根据自己能力选做，以完成上述功能为主）
"""
import random
import tkinter
from tkinter import *


def create(operate, max, decimal, dec_bit, bracket):
    Formula = []  # 生成的算式
    numBracket = 0  # 括号数量
    numCount = random.randint(2, 6)  # 运算数字数量
    if bracket:
        if numCount < 3:  # 括号数量
            numBracket = 0
        elif numCount < 5:
            numBracket = 1
            braLeft1 = random.randint(1, numCount - 1)  # 随机生成括号1的位置
            braRight1 = random.randint(2, numCount)
            while braRight1 < braLeft1:
                braRight1 = random.randint(2, numCount)
        else:
            numBracket = random.randint(0, 2)
            braLeft1 = random.randint(1, numCount - 1)  # 随机生成括号1的位置
            braRight1 = random.randint(2, numCount)
            while braRight1 < braLeft1:  # 如果)在(左边，重新生成
                braRight1 = random.randint(2, numCount)
            braLeft2 = random.randint(1, numCount - 1)  # 括号2位置
            braRight2 = random.randint(2, numCount)
            while braRight2 < braLeft2:
                braRight2 = random.randint(2, numCount)
    for i in range(numCount):
        if bracket:  # 随机添加左括号
            if numBracket == 1 and i + 1 == braLeft1:
                Formula.append('(')
            if numBracket == 2:
                if i + 1 == braLeft1:
                    Formula.append('(')
                if i + 1 == braLeft2:
                    Formula.append('(')
        if decimal:  # 随机生成小数
            digit = random.uniform(0, max)
            digit = round(digit, dec_bit)  # 小数精度
        else:  # 随机生成整数
            digit = random.randint(0, max)
        Formula.append(digit)
        # 添加右括号
        if bracket:
            if numBracket == 1 and i + 1 == braRight1:
                Formula.append(')')
            if numBracket == 2:
                if i + 1 == braRight1:
                    Formula.append(')')
                if i + 1 == braRight2:
                    Formula.append(')')
        # 数字后添加算符
        if i != numCount - 1:
            Formula.append(operate[random.randint(0, len(operate) - 1)])
    buf = [str(i) for i in Formula]
    s = ''.join(buf)
    return s


# 查看问题的解答
def view_answers():
    value = lbox.get(lbox.curselection())  # 获取当前选中的文本
    var1.set(round(eval(str(value)), 2))  # 为label设置值


# 获取输入的数据
def inputdata():
    lbox.delete(1, END)  # 清空上次生成的题目

    num = var_num.get()
    num = int(num)
    operate = []
    if op1.get() == '+':
        operate.append('+')
    if op2.get() == '-':
        operate.append('-')
    if op3.get() == '*':
        operate.append('*')
    if op4.get() == '/':
        operate.append('/')
    max = var_max.get()
    max = int(max)
    decimal = var_dec.get()
    decimal = int(decimal)
    dec_bit = var_bit.get()
    dec_bit = int(dec_bit)
    bracket = var_bra.get()
    bracket = int(bracket)
    for i in range(num):
        s = create(operate, max, decimal, dec_bit, bracket)
        lbox.insert('end', s)


if __name__ == '__main__':
    # 创建窗口
    win = tkinter.Tk()
    win.title("四则运算生成器")
    win.geometry("600x600")
    # 创建选项
    tkinter.Label(win, text='题目数量：').place(x=10, y=150)
    var_num = tkinter.StringVar()
    entry_num = tkinter.Entry(win, textvariable=var_num)
    entry_num.place(x=80, y=150)

    tkinter.Label(win, text='操作符：').place(x=10, y=180)
    op1 = StringVar()
    op2 = StringVar()
    op3 = StringVar()
    op4 = StringVar()
    check1 = tkinter.Checkbutton(win, text='+', font=("Times New Roman", "16"), variable=op1, onvalue='+', offvalue='').place(x=80, y=170)
    check2 = tkinter.Checkbutton(win, text='-', font=("Times New Roman", "16"), variable=op2, onvalue='-', offvalue='').place(x=140, y=170)
    check3 = tkinter.Checkbutton(win, text='*', font=("Times New Roman", "16"), variable=op3, onvalue='*', offvalue='').place(x=200, y=170)
    check4 = tkinter.Checkbutton(win, text='/', font=("Times New Roman", "16"), variable=op4, onvalue='/', offvalue='').place(x=260, y=170)

    tkinter.Label(win, text='数字最大值：').place(x=10, y=210)
    var_max = tkinter.StringVar()
    entry_max = tkinter.Entry(win, textvariable=var_max)
    entry_max.place(x=80, y=210)

    tkinter.Label(win, text='是否有小数?').place(x=10, y=240)
    var_dec = tkinter.StringVar()
    var_dec.set('1')
    radio1 = tkinter.Radiobutton(win, variable=var_dec, value='1', text='是').place(x=80, y=240)
    radio1 = tkinter.Radiobutton(win, variable=var_dec, value='0', text='否').place(x=150, y=240)

    tkinter.Label(win, text='请输入精度：').place(x=10, y=270)
    var_bit = tkinter.StringVar()
    entry_bit = tkinter.Entry(win, textvariable=var_bit)
    entry_bit.place(x=80, y=270)

    tkinter.Label(win, text='是否有括号?').place(x=10, y=300)
    var_bra = tkinter.StringVar()
    var_dec.set('1')
    radio2 = tkinter.Radiobutton(win, variable=var_bra, value='1', text='是').place(x=80, y=300)
    radio2 = tkinter.Radiobutton(win, variable=var_bra, value='0', text='否').place(x=150, y=300)

    button_enter = tkinter.Button(win, text='点击生成题目', bg='orange', command=inputdata)
    button_enter.place(x=100, y=330)
    # 创建答案区
    var1 = tkinter.StringVar()
    lab1 = tkinter.Label(win, bg='yellow', width=20, height=2, textvariable=var1)
    lab1.pack()
    # 创建查看答案按钮
    button1 = tkinter.Button(win, text='点此查看算式答案', width=15, height=2, command=view_answers, bg='orange')
    button1.pack()
    var2 = tkinter.StringVar()
    var2.set('以下为生成的算式：')
    # 创建滚动条
    scrolly = Scrollbar(win)
    scrolly.pack(side=RIGHT, fill=Y)
    # 创建Listbox（即生成算式列表）
    lbox = tkinter.Listbox(win, width=30, height=200, listvariable=var2, yscrollcommand=scrolly.set)
    lbox.pack(anchor=tkinter.NE)
    scrolly.config(command=lbox.yview)
    # 显示主窗口
    win.mainloop()
