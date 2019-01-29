import tkinter as tk

from matplotlib.figure import Figure

import tkinter
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
# Implement the default Matplotlib key bindings.
from matplotlib.backend_bases import key_press_handler

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
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()
        self.add_plot()



            


    def create_widgets(self):
        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "Can you guess the Pearson correlation between the variables X and Y?"
#        self.hi_there["command"] = self.say_hi
        self.hi_there.pack(side="top")

        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit.config (height=2, width=8)
        self.quit.pack(side="bottom")


        self.send = tk.Button(self, text="SEND", fg="green",
                              command=self.check_result)
        self.send.config (height=3, width=10)
        self.send.pack(side="bottom")


        self.input_text = tk.Entry(self)
        self.input_text.insert(0,"")
        self.input_text.pack(side="top")

        self.input_text.bind('<Key-Return>', self.on_changed)

    def on_changed(self, event):
        print (event.keysym,type(event.keysym))
        if (event.keysym=='Return'):
            self.check_result()

#    def say_hi(self):
#        print("hi there, everyone!")

    def check_result(self):
        print ("Let's check the super result!")
        value = float(self.input_text.get())
        print ("The input is:", value)
        print ("And your error is:",value-self.correlation)

        absdiff = np.abs(value-self.correlation)
        diff = value-self.correlation

        if absdiff<0.1:
            tk.messagebox.showinfo("Good job!", "You were "+str(diff)+" points far.")
        elif absdiff < 0.3:
            tk.messagebox.showwarning("Almost... Keep up!", "You were "+str(diff)+" points far.")
        else:
            tk.messagebox.showerror("Oh, gosh! No!", "You were "+str(diff)+" points far.")
        self.master.destroy()


    def add_plot(self):
        #GENERATE FIGURE:
        fig = Figure(figsize=(5, 4), dpi=100)

        #X= np.random.random((100,2))
        corr=np.random.random()
        x,y = generateCorrelatedData(corr)
        fig.add_subplot(111).scatter(x,y,s=5)


        canvas = FigureCanvasTkAgg(fig, master=root)  # A tk.DrawingArea.
        canvas.draw()
        canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

        toolbar = NavigationToolbar2Tk(canvas, root)
        toolbar.update()
        canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

        def on_key_press(event):
#            print("you pressed {}".format(event.key))
#            print (event.key,type(event.key))
            if (event.key=='enter'):
                self.check_result()
            key_press_handler(event, canvas, toolbar)
        canvas.mpl_connect("key_press_event", on_key_press)


        self.correlation = round(pearsonr(x,y)[0],2)
        print (self.correlation)


root = tk.Tk()
app = Application(master=root)









app.mainloop()

