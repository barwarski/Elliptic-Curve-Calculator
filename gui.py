import tkinter as tk
from tkinter import *
from tkinter.messagebox import showinfo
from eccGruppenop import start


class Gui(object):
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("ECC")
        self.root.geometry("350x400")

        self.frame_header = tk.Frame(self.root)
        self.frame_header.pack()
        self.label_header = tk.Label(master=self.frame_header, text="Please enter the variabels:")
        self.label_header.pack()

        self.fa = tk.Frame(self.root)
        self.fa.pack(ipadx=20, ipady=10)
        self.label_a = tk.Label(master=self.fa, text="a: ")
        self.label_a.pack(side="left")
        self.entry_a = tk.Entry(master=self.fa, bg='white')
        self.entry_a.pack(side="right")

        self.fb = tk.Frame(self.root)
        self.fb.pack(ipadx=20, ipady=10)
        self.label_b = tk.Label(master=self.fb, text="b: ")
        self.label_b.pack(side="left")
        self.entry_b = tk.Entry(master=self.fb, bg='white')
        self.entry_b.pack(side="right")

        self.fp = tk.Frame(self.root)
        self.fp.pack(ipadx=20, ipady=10)
        self.label_p = tk.Label(master=self.fp, text="p: ")
        self.entry_p = tk.Entry(master=self.fp, bg='white')
        self.label_p.pack(side="left")
        self.entry_p.pack(side="right")

        self.f_x1 = tk.Frame(self.root)
        self.f_x1.pack(ipadx=20, ipady=10)
        self.label_x1 = tk.Label(master=self.f_x1, text="x1: ")
        self.entry_x1 = tk.Entry(master=self.f_x1, bg='white')
        self.label_x1.pack(side="left")
        self.entry_x1.pack(side="right")

        self.f_y1 = tk.Frame(self.root)
        self.f_y1.pack(ipadx=20, ipady=10)
        self.label_y1 = tk.Label(master=self.f_y1, text="y1: ")
        self.entry_y1 = tk.Entry(master=self.f_y1, bg='white')
        self.label_y1.pack(side="left")
        self.entry_y1.pack(side="right")

        self.f_x2 = tk.Frame(self.root)
        self.f_x2.pack(ipadx=20, ipady=10)
        self.label_x2 = tk.Label(master=self.f_x2, text="x2: ")
        self.entry_x2 = tk.Entry(master=self.f_x2, bg='white')
        self.label_x2.pack(side="left")
        self.entry_x2.pack(side="right")

        self.f_y2 = tk.Frame(self.root)
        self.f_y2.pack(ipadx=20, ipady=10)
        self.label_y2 = tk.Label(master=self.f_y2, text="y2: ")
        self.entry_y2 = tk.Entry(master=self.f_y2, bg='white')
        self.label_y2.pack(side="left")
        self.entry_y2.pack(side="right")

        self.f_end = tk.Frame(self.root)
        self.f_end.pack()
        self.label_result = tk.Label(self.f_end, text=" click on the Button to start calculate the elip. curve")
        self.start_button = tk.Button(self.f_end, text="Start calculate", command=self.getInfo)
        self.start_button.pack(side="top")
        self.label_result.pack(side="bottom")
        self.root.mainloop()

    def calculating(self):
        pass

    def getInfo(self):
        a = int(self.entry_a.get())
        b = int(self.entry_b.get())
        p = int(self.entry_p.get())
        x1 = int(self.entry_x1.get())
        y1 = int(self.entry_y1.get())
        x2 = int(self.entry_x2.get())
        y2 = int(self.entry_y2.get())
        result = start(a, b, p, x1, y1, x2, y2)
        #result_text = "Result: " + str(result)
        newWindow = Toplevel(self.root)
        newWindow.title("Result")
        tk.Label(newWindow,text=result).pack()

