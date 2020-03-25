from tkinter import *
from tkinter import messagebox
# ---------------------------
# @description 
# @author xichengxml
# @date 2020/3/22 下午 05:24
# ---------------------------


root = Tk()

btn01 = Button(root)
btn01["text"] = "点我送花"
btn01.pack()


def send_flower(e):
    messagebox.showinfo("Message", "你好，送你一朵鲜花")
    print("送花成功~")


btn01.bind("<Button-1>", send_flower)
root.mainloop()


