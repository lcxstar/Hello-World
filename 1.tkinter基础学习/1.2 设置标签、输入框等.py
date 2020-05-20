# 在完成窗口设置后，需要给窗口中添加标签、输入框

from tkinter import Tk , messagebox,Toplevel

# 设置内部组件，也可以使用上面的导入方式
import tkinter as tk

my_window = Tk()
my_window.title('我的窗口')
screen_width, screen_height = my_window.maxsize()
width = 250
height = 250
align_str = '%dx%d+%d+%d'%(width,height,(screen_width-width)/2,(screen_height-height)/2)
my_window.geometry(align_str)
my_window.resizable(width=False,height=False)

# 设置标签，标签位置，大小等。text参数将显示在定义的位置，font参数中放置 字体、字号
user_name_label = tk.Label(my_window,text='账号',font=('FangSong',14))
user_name_label.place(x=30,y=30)
user_pwd_label = tk.Label(my_window,text='密码',font=('FangSong',14))
user_pwd_label.place(x=30,y=80)

# 设置输入框
# （1）输入框文本设置，输入内容为字符型数据
user_name_text = tk.StringVar()
user_name_text.set('输入账号')
# （2）输入框大小设置，Entry的参数有4个，①输入框的所在窗口名 ②字符串的内容 ③字体 ④输入框的宽度
user_name_entry = tk.Entry(my_window,textvariable=user_name_text,font=('FangSong',14),width = 15)
# （3）输入框位置设置
user_name_entry.place(x=80,y=30)

user_pwd_text = tk.StringVar()
user_pwd_text.set('输入密码')
user_pwd_entry = tk.Entry(my_window,textvariable=user_pwd_text,font=('FangSong',14),width = 15)
user_pwd_entry.place(x=80,y=80)

# 数据读取，此处需要一个data.txt文件，文件中每行的内容格式类似 admin:123
def read_data():
    with open('data.txt','r') as f:
        # 按行读取数据
        rows = f.readlines()
        # 定义一个空列表，将读取结果按字典形式保存
        user_info_dict={}
        for row in rows:
            dict_list = row.strip().split(":")
            user_info_dict[dict_list[0]] = dict_list[1]
        # 关闭文件流
        f.close()
        return user_info_dict

# 登录事件回调函数，点击登录按钮将实现函数中的功能
def use_login():
    # 获取用户输入的账号和密码，将用户输入的数据赋值给变量
    name = user_name_text.get()
    pwd = user_pwd_text.get()
    user_dict = read_data()
    # 比较输入数据与data.txt文件已有的数据是否一致，根据判断结果弹出相应的信息
    if name != ''and pwd != '':
        if name in user_dict.keys():
            if pwd == user_dict[name]:
                # print('ok')
                messagebox.showinfo(title='成功',message='欢迎'+name+'到来')
            else:
                # print('密码不正确')
                messagebox.showerror(title='错误', message='密码不正确')
        else:
            # print('用户不存在')
            messagebox.showerror(title='错误', message='用户不存在')
    else:
        # print('账号密码不能为空')
        messagebox.showerror(title='错误',message='账号、密码不能为空')

# 注册事件回调函数，点击注册按钮将实现函数中的功能
def pop_win():
    # 弹出一个子窗口
    top = Toplevel()
    top.title('注册')
    top.geometry('250x200')
    
    # 账号、密码、确认密码、注册按钮
    # 窗口中内容的布局方式有两种，place：通过x，y坐标的方式进行定位，grid：按行和列的方式定位
    tk.Label(top,text='账号',width=10).grid(row=1,column=0)
    user_name = tk.StringVar()
    tk.Entry(top,textvariable=user_name,width=15).grid(row=1,column=1)
    tk.Label(top, text='密码', width=10).grid(row=2, column=0)
    
    user_pwd = tk.StringVar()
    tk.Entry(top, textvariable=user_pwd, width=15).grid(row=2, column=1)
    tk.Label(top, text='确认密码', width=10).grid(row=3, column=0)
    user_confirm_pwd = tk.StringVar()
    tk.Entry(top, textvariable=user_confirm_pwd, width=15).grid(row=3, column=1)
    
    # 子窗口中注册事件的回调函数
    def user_register():
        # 获取输入框的值
        name = user_name.get()
        pwd = user_pwd.get()
        confirm_pwd = user_confirm_pwd.get()
        if pwd == confirm_pwd:
            with open('data.txt','a') as f:
                f.writelines("\n"+name+":"+pwd)
                f.flush()
                f.close()
                messagebox.showinfo(title='成功',message='注册成功')
                # 关闭子窗口
                top.destroy()
        else:
            messagebox.showerror(title='错误',message='两次密码不一致')
    # 子窗口按钮设置 columnspan将量列合并为一列，pady调整与上面一行的间距
    tk.Button(top,text='注册',width=15,command=user_register).grid(row=4,columnspan=2,pady=15)


# 主窗口按钮设置，command参数后面直接加函数名
user_login_button = tk.Button(my_window,text='登录',font=('FangSong',14),command=use_login)
user_login_button.place(x=30,y=130)

user_reg_button = tk.Button(my_window,text='注册',font=('FangSong',14),command=pop_win)
user_reg_button.place(x=180,y=130)

my_window.mainloop()
