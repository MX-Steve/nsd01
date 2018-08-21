# yum install -y tk-devel tcl-devel sqlite-devel
# cd /opt
# tar zxf Python3.6.1...tar.gz
# cd Python3.6.1
# ./configure --prefix=/usr/local
# make
# make install
# tkinter 图形窗口，python自带，只是没装
import tkinter
from functools import partial

root = tkinter.Tk()
lb1 = tkinter.Label(root, text="Hello World", font='Arial 15')
MyButton = partial(tkinter.Button, root, bg="blue", fg="white", text='hello world!')
b1 = MyButton(text="Button 1")
b2 = MyButton(text="Button 2")
b3 = MyButton(text="Button 3", command=root.quit)

lb1.pack()
b1.pack()
b2.pack()
b3.pack()

root.mainloop()
