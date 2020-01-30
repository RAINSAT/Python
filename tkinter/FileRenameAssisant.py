# -*- coding: utf-8 -*-

import tkinter as tk
from tkinter import filedialog
from tkinter import Entry
from tkinter import messagebox
from tkinter import PhotoImage
import os


class WidgetAssisant(object):
    def __init__(self):
        pass

    @staticmethod
    def get_screen_size(window):
        return window.winfo_screenwidth(), window.winfo_screenheight()


class QApplication(object):
    def __init__(self, master):

        self.root = master
        self.initWidget()

    def exec_loop(self):
        if self.root is not None:
            self.root.mainloop()

    def initWidget(self):
        if self.root is not None:
            # 最大最小尺寸
            self.root.maxsize(1920, 1080)
            self.root.minsize(480, 300)
            width, height, padx, pady = 1366, 768, 10, 10
            # 标题
            self.root.title("FileRenameAssisant")
            # 屏幕居中
            screen_width, screen_height = WidgetAssisant.get_screen_size(
                self.root)
            self.root.geometry("%dx%d+%d+%d" % (width, height,
                                                (screen_width - width) / 2, (screen_height - height) / 2))
            # 控件
            self.__frame_top = tk.Frame(master=self.root)
            self.__frame_top.pack(side=tk.TOP, padx=10, pady=10)
            self.entry_dir = tk.Entry(
                self.__frame_top, bd=5, width=100)
            self.entry_dir.pack(side=tk.LEFT)
            self.button_rename = tk.Button(
                self.__frame_top, text="重命名", foreground="blue", command=self.__on_button_rename_clicked)
            self.button_rename.pack(side=tk.RIGHT)
            self.button_open = tk.Button(
                self.__frame_top, text="打开目录", foreground="blue", command=self.__on_button_open_clicked)
            self.button_open.pack(side=tk.RIGHT)

            self.__frame_bottom = tk.Frame(master=self.root)
            self.__frame_bottom.pack(side=tk.BOTTOM, padx=10, pady=10)
            self.listBox = tk.Listbox(
                self.__frame_bottom, width=30, height=750)
            self.labelPic = tk.Label(
                self.__frame_bottom, foreground="blue", text="Python", width=500, height=750)

            self.listBox.pack(side=tk.LEFT)
            self.labelPic.pack(side=tk.LEFT)

            # self.listBox.bind("<Double-Button-1>", self.__on_listbox_dc)

    def __on_button_open_clicked(self):
        self.entry_dir.delete(0, tk.END)
        dir = filedialog.askdirectory(
            title="打开目录", initialdir=os.path.expanduser("./"))
        self.entry_dir.insert(0, dir)
        os.chdir(dir)
        file_list = os.listdir()
        for i in range(0, file_list.__len__()):
            self.listBox.insert(i, file_list[i])

    def __on_button_rename_clicked(self):
        pass


app = QApplication(tk.Tk())


# 主消息循环:
app.exec_loop()
