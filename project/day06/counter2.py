import tkinter
from functools import partial

def hello():
    lb1.config(text="Hello china")

def welcome():
    lb1.config(text="hello tedu")

def sayhi(word):
    def greet():
        lb1.config(text="hello %s" % word)
    return greet

root = tkinter.Tk()
lb1 = tkinter.Label(root, text="Hello World", font='Arial 15')
MyButton = partial(tkinter.Button, root, bg="blue", fg="white", text='hello world!')
b1 = MyButton(text="Button 1",command=sayhi("China"))
b2 = MyButton(text="Button 2",command=sayhi("tedu"))
b3 = MyButton(text="Button 3", command=root.quit)

lb1.pack()
b1.pack()
b2.pack()
b3.pack()

root.mainloop()
