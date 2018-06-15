#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2018/6/7 15:35
# @Author : Aries
# @Site : 
# @File : Pannel.py
# @Software: PyCharm
from Tkinter import *
from tkMessageBox import *
from Command import *

class Reg (Frame):
    def __init__(self,master):
        self.keydict = dict()

        frame = Frame(master)
        frame.pack()
        self.lab1 = Label(frame,text = "Host:")
        self.lab1.grid(row = 0,column = 0)
        self.host = Entry(frame)
        self.host.grid(row = 0,column = 1,columnspan=2,sticky = W)
        self.lab2 = Label(frame,text = "Ping包个数:")
        self.lab2.grid(row = 1,column = 0)
        self.count = Entry(frame)
        self.count.grid(row = 1,column = 1, columnspan=2)
        self.lab3 = Label(frame, text="Ping包间隔(ms):")
        self.lab3.grid(row=2, column=0)
        self.time = Entry(frame)
        self.time.grid(row=2, column=1,columnspan=2)
        self.lab4 = Label(frame, text="Ping包大小(b):")
        self.lab4.grid(row=3, column=0)
        self.size = Entry(frame)
        self.size.grid(row=3, column=1, columnspan=2)

        self.button = Button(frame,text = "测试",command = self.Submit)
        self.button.grid(row = 5,column = 0,sticky = W)
        self.button2 = Button(frame,text = "退出",command = frame.quit)
        self.button2.grid(row = 5,column = 2,sticky = E)

    def getkeys(self):
        self.keydict['n'] = self.count.get()
        self.keydict['t'] = self.time.get()
        self.keydict['s'] = self.size.get()

    def Submit(self):
        self.getkeys()
        host = self.host.get()
        cmd = parseCmd(self.keydict, host)
        result = execCmd(cmd)
        writeFile('result/pings.txt', result)
        showinfo('Message', 'Results written in result/pings.txt')
root = Tk()
root.title("FPing Kit")
app = Reg(root)
root.mainloop()