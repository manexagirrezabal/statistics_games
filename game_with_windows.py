

import tkinter as tk



#master=Tk()

class Application(tk.Frame):
    def __init__(self, master=None, n=5):
        super().__init__(master)
        self.master = master
        #self.pack()
        #self.create_widgets()
        #self.add_plot()
        self.p=[0]*n
        for i in range(n):
#            p[i]=makeframe(i, self.master)
            print ("Create frame no.",i)
            self.i=i
            self.p[i] = {}
            self.p[i]['frame']=tk.Frame(self.master)
            self.p[i]['nextbutton']=tk.Button(self.p[i]['frame'],text='next',command=self.next,compound=tk.BOTTOM)
            self.p[i]['nextbutton'].grid(column=2,row=0)
            self.p[i]['backbutton']=tk.Button(self.p[i]['frame'],text='back',command=self.back,compound=tk.BOTTOM)
            self.p[i]['backbutton'].grid(column=0,row=0)
            self.p[i]['label']=tk.Label(self.p[i]['frame'],text='Exercise no. %i'%(self.i+1)).grid(column=1,row=0)
        self.currentwindow=0

        self.p[self.currentwindow]['frame'].grid()
        self.p[self.currentwindow]['backbutton'].config(state=tk.DISABLED)
        self.p[-1]['nextbutton'].config(state=tk.DISABLED)

    def next(self):
        self.p[self.currentwindow]['frame'].grid_forget()
        self.currentwindow +=1
        self.p[self.currentwindow]['frame'].grid()

    def back(self):
        self.p[self.currentwindow]['frame'].grid_forget()
        self.currentwindow -=1
        self.p[self.currentwindow]['frame'].grid()


#class makeframe(object):
#    def __init__(self,i, master):




#master.mainloop()

root = tk.Tk()
app = Application(master=root, n=7)

app.mainloop()


