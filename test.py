import tkinter as Tkinter
import os


os.environ.__setitem__('DISPLAY', '0.0')
master = Tkinter.Tk()
master.title("tester")
master.geometry("300x100")


#make a label for the window
label1 = Tkinter.Label(master, text='Hellooooo')
# Lay out label
label1.pack()

# Run forever!
master.mainloop()