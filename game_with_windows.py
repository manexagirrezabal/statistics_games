

import tkinter as tk



class Application(tk.Frame):
    def __init__(self, master=None, n=5):
        super().__init__(master)
        self.master = master
        self.p = []
        for i in range(n):
            print ("Create frame no.",i)

            frame=tk.Frame(self.master)
            frame.nextbutton=tk.Button(frame,text='next',command=self.next,compound=tk.BOTTOM)
            frame.nextbutton.grid(column=2,row=0)
            frame.backbutton=tk.Button(frame,text='back',command=self.back,compound=tk.BOTTOM)
            frame.backbutton.grid(column=0,row=0)
            frame.label=tk.Label(frame,text='Exercise no. %i'%(i+1)).grid(column=1,row=0)
            self.p.append(frame)

        self.currentwindow=0

        self.p[self.currentwindow].grid()
        self.p[self.currentwindow].backbutton.config(state=tk.DISABLED)
        self.p[-1].nextbutton.config(state=tk.DISABLED)

    def next(self):
        self.p[self.currentwindow].grid_forget()
        self.currentwindow +=1
        self.p[self.currentwindow].grid()

    def back(self):
        self.p[self.currentwindow].grid_forget()
        self.currentwindow -=1
        self.p[self.currentwindow].grid()




root = tk.Tk()
app = Application(master=root, n=7)

app.mainloop()


