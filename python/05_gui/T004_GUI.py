from tkinter import *
from tkinter import messagebox

# ---------------------------
# @description 一个经典的Application
# @author xichengxml
# @date 2020/3/26 上午 01:15
# ---------------------------


class MyApplication(Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()

        self.create_widget()

    def create_widget(self):
        # 创建一个按钮
        self.btn01 = Button(self)
        self.btn01['text'] = '送花'
        self.btn01.pack()
        self.btn01['command'] = self.send_flower
        # 创建一个退出按钮
        self.btnQuit = Button(self, text='退出', command=self.master.destroy)
        self.btnQuit.pack()

    def send_flower(self):
        messagebox.showinfo("送花", "999朵桃花")


if __name__ == '__main__':
    root = Tk()
    root.geometry("800x600+100+100")
    root.title("一个经典的GUI案例")
    MyApplication(master=root)
    root.mainloop()
