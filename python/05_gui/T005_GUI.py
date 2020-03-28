from tkinter import *

# ---------------------------
# @description label组件
# @author xichengxml
# @date 2020/3/28 下午 05:57
# ---------------------------


class MyLabel(Frame):

    def __init__(self, master=None):

        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widget()

    def create_widget(self):

        self.label01 = Label(self, text='梦境阁', width=10, height=1, bg='black', fg='white')
        self.label01.pack()

        self.label02 = Label(self, text='西城xml', width=10, height=2, bg='blue', fg='white')
        self.label02.pack()

        # 将image声明成global，否则方法执行完之后，对象消失，无法显示图片
        global image
        # 默认只能识别gif格式文件
        image = PhotoImage(file='img/梦境阁.gif')
        self.label03 = Label(self, image=image, width=400, height=300)
        self.label03.pack()

        self.label04 = Label(self, text='梦境阁\n西城xml\n开着终极爆天甲, 天天练图', borderwidth=1, relief='solid', justify='right')
        self.label04.pack()


if __name__ == '__main__':
    root = Tk()
    root.geometry('800x600+100+100')
    MyLabel(root)
    root.mainloop()

