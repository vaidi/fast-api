from tkinter import Tk
from tkinter.ttk import Label,Button

tk_obj = Tk()

# 设置窗口标题
tk_obj.title("你最美")

#填加标签
label = Label(tk_obj,text="hello world")
label.pack()

def on_click():
    label.config(text="Button clicked|")

button = Button(tk_obj,text="click me",command=on_click)

button.pack()


# 设置窗口大小（格式："宽度x高度"）
tk_obj.geometry("500x300")

# 运行主循环（保持窗口显示）
tk_obj.mainloop()