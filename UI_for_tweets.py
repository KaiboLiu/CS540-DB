#coding=utf-8
#!/usr/bin/python
# downloaded, Feet to Meters calculator



#from Tkinter import *

from Tkinter import *
import ttk

def calculate(*args):
    try:
        value = float(feet.get())
        #meters.set((0.3048 * value * 10000.0 + 0.5)/10000.0)
        meters.set(a)
    except ValueError:
        pass
a = 6
root = Tk()
root.title("Twitter classification")
sty = ttk.Style()
sty.configure('my.TButton', font=('Helvetica', 30, 'bold'))
sty1 = ttk.Style()
sty1.configure('my.Label', font=('Helvetica', 30))

mainframe = ttk.Frame(root, padding="20 20 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)
feet = StringVar()
meters = StringVar()
feet_entry = ttk.Entry(mainframe, width=40, textvariable=feet,font=('Arial', 30))
feet_entry.grid(column=2, row=1, sticky=(W, E))
ttk.Label(mainframe, textvariable=meters,font=('Arial', 30,'italic'),foreground='#1478e2').grid(column=2, row=3, sticky=(W, E))
ttk.Button(mainframe, text="Predict", style='my.TButton', command=calculate).grid(column=2, row=5, sticky=W)
ttk.Label(mainframe, text="Input your tweet", style='my.Label').grid(column=1, row=1, sticky=W)
ttk.Label(mainframe, text="Your tweet is more like", style='my.Label').grid(column=1, row=3, sticky=E)
ttk.Label(mainframe, text="style", style='my.Label').grid(column=3, row=3, sticky=W)
for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)
feet_entry.focus()
root.bind('<Return>', calculate)
root.mainloop()
