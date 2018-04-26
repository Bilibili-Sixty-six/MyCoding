# -*- coding: UTF-8 -*-
from Tkinter import Tk, Label, Button, mainloop
from math import sqrt, sin, cos, tan, log10, log, factorial


def main():
    """计算器的GUI"""
    # 根窗口初始化------------------------------------------------------------------------------------------------------

    root = Tk()  # 根窗口
    root.title('Calculator')  # 窗口标题
    root.resizable(False, False)  # 不可缩放

    # GUI布局-----------------------------------------------------------------------------------------------------------

    # 计算器的“显示屏幕”
    queue = ['0']  # eval()处理''会产生异常故初始化一个'0'

    label = Label(root, justify='right', text=queue, width=40, height=2, anchor='e')
    label.grid(row=0, columnspan=7)  # “屏幕”初始化

    def deal_buttons(button):
        """处理数字和运算符按钮的返回值"""
        i = len(button)  # 非简单的数字和运算符的grid单元的title长度被设定为大于3，特殊处理
        if queue[0] == '0' and (button in ('1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '00', '(', ')')):
            "处理最前面无用的0"
            queue.pop(0)
        print button
        end = ''.join(queue)

        if i < 3:
            queue.append(button)
        elif i == 3:
            queue.append(button + '(')
        elif button == ' × ':
            queue.append('*')
        elif button == ' ÷ ':
            queue.append('/')
        elif button == '  =  ':
            try:
                queue[:] = [str(eval(end))]
            except SyntaxError:
                queue[:] = [str(eval(end + ')'))]   # 补上缺少的一个括号
            except TypeError:
                queue[:] = ['0']    # 错误输入直接返回0
        elif button == ' √ ':
            queue.append('sqrt(')
        elif button == '  ^  ':
            queue.append('**')
        elif button == ' lg ':
            queue.append('log10(')
        elif button == ' ln ':
            queue.append('log(')
        elif button == ' X! ':
            queue.insert(-2, 'factorial(')
        elif button == ' ← ':
            queue.pop()
            if queue == []:
                queue.append('0')
        elif button == '  C  ':
            queue[:] = ['0']
        elif button == ' OFF ':
            root.quit()

        end = ''.join(queue)  # 实时更新
        # print end
        return end

    def foo(arg):
        label.config(text=deal_buttons(arg))
        # label.after(1)

    """
        # 功能按钮部署
    r = 1   # 按钮行初始值
    c = 0   # 按钮列初始值

    BUG: button
    for button in buttons:
        Button(root, text=button, command=lambda: label.config(text=deal_buttons(button)))\
            .grid(row=r, column=c, sticky='nesw')
        # 参数nesw意为与上下左右各个方向邻近单元对齐
        if r < 5:
            r += 1
            continue
        r = 1
        c += 1
    """
    # -----------------------------------------------------------------------------

    Button(root, text='(', command=lambda: label.config(text=deal_buttons('('))) \
        .grid(row=1, column=0, sticky='nesw')
    Button(root, text='  ^  ', command=lambda: label.config(text=deal_buttons('  ^  '))) \
        .grid(row=2, column=0, sticky='nesw')
    Button(root, text=' lg ', command=lambda: label.config(text=deal_buttons(' lg '))) \
        .grid(row=3, column=0, sticky='nesw')
    Button(root, text=' ln ', command=lambda: label.config(text=deal_buttons(' ln '))) \
        .grid(row=4, column=0, sticky='nesw')
    Button(root, text=' X! ', command=lambda: label.config(text=deal_buttons(' X! '))) \
        .grid(row=5, column=0, sticky='nesw')
    Button(root, text=')', command=lambda: label.config(text=deal_buttons(')'))) \
        .grid(row=1, column=1, sticky='nesw')
    Button(root, text=' √ ', command=lambda: label.config(text=deal_buttons(' √ '))) \
        .grid(row=2, column=1, sticky='nesw')
    Button(root, text='sin', command=lambda: label.config(text=deal_buttons('sin'))) \
        .grid(row=3, column=1, sticky='nesw')
    Button(root, text='cos', command=lambda: label.config(text=deal_buttons('cos'))) \
        .grid(row=4, column=1, sticky='nesw')
    Button(root, text='tan', command=lambda: label.config(text=deal_buttons('tan'))) \
        .grid(row=5, column=1, sticky='nesw')
    Button(root, text='%', command=lambda: label.config(text=deal_buttons('%'))) \
        .grid(row=1, column=2, sticky='nesw')
    Button(root, text=' × ', command=lambda: label.config(text=deal_buttons(' × '))) \
        .grid(row=2, column=2, sticky='nesw')
    Button(root, text=' ÷ ', command=lambda: label.config(text=deal_buttons(' ÷ '))) \
        .grid(row=3, column=2, sticky='nesw')
    Button(root, text='+', command=lambda: label.config(text=deal_buttons('+'))) \
        .grid(row=4, column=2, sticky='nesw')
    Button(root, text='-', command=lambda: label.config(text=deal_buttons('-'))) \
        .grid(row=5, column=2, sticky='nesw')
    Button(root, text=' mc ', command=lambda: label.config(text=deal_buttons(' mc '))) \
        .grid(row=1, column=3, sticky='nesw')
    Button(root, text='7', command=lambda: label.config(text=deal_buttons('7'))) \
        .grid(row=2, column=3, sticky='nesw')
    Button(root, text='4', command=lambda: label.config(text=deal_buttons('4'))) \
        .grid(row=3, column=3, sticky='nesw')
    Button(root, text='1', command=lambda: label.config(text=deal_buttons('1'))) \
        .grid(row=4, column=3, sticky='nesw')
    Button(root, text='0', command=lambda: label.config(text=deal_buttons('0'))) \
        .grid(row=5, column=3, sticky='nesw')
    Button(root, text=' m+ ', command=lambda: label.config(text=deal_buttons(' m+ '))) \
        .grid(row=1, column=4, sticky='nesw')
    Button(root, text='8', command=lambda: label.config(text=deal_buttons('8'))) \
        .grid(row=2, column=4, sticky='nesw')
    Button(root, text='5', command=lambda: label.config(text=deal_buttons('5'))) \
        .grid(row=3, column=4, sticky='nesw')
    Button(root, text='2', command=lambda: label.config(text=deal_buttons('2'))) \
        .grid(row=4, column=4, sticky='nesw')
    Button(root, text='00', command=lambda: label.config(text=deal_buttons('00'))) \
        .grid(row=5, column=4, sticky='nesw')
    Button(root, text=' m- ', command=lambda: label.config(text=deal_buttons(' m- '))) \
        .grid(row=1, column=5, sticky='nesw')
    Button(root, text='9', command=lambda: label.config(text=deal_buttons('9'))) \
        .grid(row=2, column=5, sticky='nesw')
    Button(root, text='6', command=lambda: label.config(text=deal_buttons('6'))) \
        .grid(row=3, column=5, sticky='nesw')
    Button(root, text='3', command=lambda: label.config(text=deal_buttons('3'))) \
        .grid(row=4, column=5, sticky='nesw')
    Button(root, text='.', command=lambda: label.config(text=deal_buttons('.'))) \
        .grid(row=5, column=5, sticky='nesw')
    Button(root, text=' mr ', command=lambda: label.config(text=deal_buttons(' mr '))) \
        .grid(row=1, column=6, sticky='nesw')
    Button(root, text=' ← ', command=lambda: label.config(text=deal_buttons(' ← '))) \
        .grid(row=2, column=6, sticky='nesw')
    Button(root, text='  C  ', command=lambda: label.config(text=deal_buttons('  C  '))) \
        .grid(row=3, column=6, sticky='nesw')
    Button(root, text=' OFF ', command=lambda: label.config(text=deal_buttons(' OFF '))) \
        .grid(row=4, column=6, sticky='nesw')
    Button(root, text='  =  ', command=lambda: label.config(text=deal_buttons('  =  '))) \
        .grid(row=5, column=6, sticky='nesw')

    # ------------------------------------------------------------------------------

    mainloop()  # 启动窗口


if __name__ == '__main__':
    main()
