
#ALSO FROM https://stackoverflow.com/questions/11100380/solution-python3-tkinter-jump-from-one-window-to-another-with-back-and-next-but

from tkinter import *



master=Tk()

class makeframe(object):
    def __init__(self,i):
        self.i=i
        self.frame=Frame(master)
        self.nextbutton=Button(self.frame,text='next',command=self.next)
        self.nextbutton.grid(column=2,row=0)
        self.backbutton=Button(self.frame,text='back',command=self.back)
        self.backbutton.grid(column=0,row=0)
        self.label=Label(self.frame,text='%i'%(self.i+1)).grid(column=1,row=0)
    def next(self):
        self.frame.grid_forget()
        p[self.i+1].frame.grid()
    def back(self):
        self.frame.grid_forget()
        p[self.i-1].frame.grid()

n=7
p=[0]*n
for i in range(n):
    p[i]=makeframe(i)
p[0].frame.grid()
p[0].backbutton.config(state=DISABLED)
p[-1].nextbutton.config(state=DISABLED)

master.mainloop()