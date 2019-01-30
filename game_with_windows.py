

import tkinter as tk

from matplotlib.figure import Figure
#import matplotlib
#matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
import numpy as np

from scipy.stats import pearsonr


def generateCorrelatedData(corr):
    xx = np.array([-0.51, 51.2])
    yy = np.array([0.33, 51.6])
    means = [xx.mean(), yy.mean()]  
    stds = [xx.std() / 3, yy.std() / 3]

    covs = [[stds[0]**2          , stds[0]*stds[1]*corr], 
        [stds[0]*stds[1]*corr,           stds[1]**2]] 

    x,y = np.random.multivariate_normal(means, covs, 1000).T
    return x,y

#Got from https://stackoverflow.com/questions/9232256/round-up-to-second-decimal-place-in-python/9232295#9232295
def round_up(x, place):
    return round(x + 5 * 10**(-1 * (place + 1)), place)


class Application(tk.Frame):
    def __init__(self, master=None, n=5):
        super().__init__(master)
        self.master = master
        self.p = []
        for i in range(n):
            print ("Create frame no.",i)
            

            frame=tk.Frame(self.master)
            frame.nextbutton=tk.Button(frame,text='next',command=self.next,compound=tk.BOTTOM)
            frame.nextbutton.grid(column=5,row=3)
            frame.backbutton=tk.Button(frame,text='back',command=self.back,compound=tk.BOTTOM)
            frame.backbutton.grid(column=0,row=3)
            frame.label=tk.Label(frame,text='Exercise no. %i: Can you guess the correlation?'%(i+1)).grid(column=0,row=0)

            frame.input_text = tk.Entry(frame)
            frame.input_text.insert(0,"")
            frame.input_text.grid(column=1, row=0)

            frame.input_text.bind('<Key-Return>', self.on_changed)



            frame.x, frame.y, frame.correlation = self.create_data(i) #I know this is not part of the frame, but it's easy to store info like this
            self.p.append(frame)

            self.add_plot(i)            



        self.currentwindow=0

        self.p[self.currentwindow].grid()
        self.p[self.currentwindow].backbutton.config(state=tk.DISABLED)
        self.p[-1].nextbutton.config(state=tk.DISABLED)


    def on_changed(self, event):
        print (event.keysym,type(event.keysym))
        if (event.keysym=='Return'):
            self.check_result()

    def check_result(self):
        print ("Let's check the super result!")
        value = float(self.p[self.currentwindow].input_text.get())
        correlation = self.p[self.currentwindow].correlation
        print ("The input is:", value)
        print ("And your error is:",value-correlation)

        absdiff = np.abs(value-correlation)
        diff = value-correlation

        if absdiff<0.1:
            tk.messagebox.showinfo("Good job!", "The actual correlation was "+str(correlation))
        elif absdiff < 0.3:
            tk.messagebox.showwarning("Almost... Keep up!", "The actual correlation was "+str(correlation))
        else:
            tk.messagebox.showerror("Oh, gosh! No!", "The actual correlation was "+str(correlation))

        self.check_all_values()

    def check_all_values(self):
        values = np.array([eachf.input_text.get()  for eachf in self.p])
        if np.sum(values=="")==0:
            actual_correlations = np.array([eachf.correlation for eachf in self.p])
            print (values.astype(float))
            #TODO CHECK SCORE AND SHOW IT!


    def next(self):
        self.p[self.currentwindow].grid_forget()
        self.currentwindow +=1
        self.p[self.currentwindow].grid()

    def back(self):
        self.p[self.currentwindow].grid_forget()
        self.currentwindow -=1
        self.p[self.currentwindow].grid()

    def add_plot(self,i):
        fig = Figure(figsize=(5, 4), dpi=100)
        fig.add_subplot(111).scatter(self.p[i].x,self.p[i].y,s=5)
        canvas = FigureCanvasTkAgg(fig, master=self.p[i])
        canvas.draw()
        canvas.get_tk_widget().grid(column=0,row=2)


    def create_data(self, i):

        corr=np.random.random()
        x,y = generateCorrelatedData(corr)
        correlation = round(pearsonr(x,y)[0],2)

        return x,y,correlation

#        fig = Figure(figsize=(5, 4), dpi=100)
#        fig.add_subplot(111).scatter(x,y,s=5)


#        canvas = FigureCanvasTkAgg(fig, master=self)  # A tk.DrawingArea.
#        canvas = FigureCanvasTkAgg(fig, master=self.p[0])  # A tk.DrawingArea.
#        canvas.draw()
#        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

#        toolbar = NavigationToolbar2Tk(canvas, self.master)
#        toolbar.update()
#        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)



root = tk.Tk()
app = Application(master=root, n=3)

app.mainloop()


