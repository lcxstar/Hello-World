# GUI（Graphical User Interface）意为图形用户界面，tkinter 提供的该功能

# Tk的功能是设置主窗口
from tkinter import Tk

# 显示窗口
my_window = Tk()
# 标题
my_window.title('我的窗口')

# 设置窗口居中
# （1）获取当前屏幕大小
screen_width, screen_height = my_window.maxsize()
# （2）设置窗口的大小
width = 480
height = 480
# （3）geometry函数只能识别字符串，所以对数据进行封装
align_str = '%dx%d+%d+%d'%(width,height,(screen_width-width)/2,(screen_height-height)/2)
# （4）设置窗口的宽，高及位置
my_window.geometry(align_str)

# 设置窗口是否可以缩放 True表示可以缩放，False表示不能缩放，默认为True
my_window.resizable(width=False,height=False)

# 显示设置好的窗口
my_window.mainloop()
