import tkinter as tk
from tkinter import Canvas,HORIZONTAL
from tkinter.ttk import *
from tkinter.ttk import Progressbar
import time
from numpy import load
# load array
import webbrowser
from tkinter import *
from matplotlib import colors
import matplotlib.pyplot as plt
from matplotlib.figure import Figure 
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
import test_truss
from loads1 import load2
import numpy as np
import matplotlib.colors
from boundary import BC
#import data
def write_slogan():
    print("Tkinter is easy to use!")

root = tk.Tk()
root.grid()
X=[0]
Y=[0]
rec=[]
array=[]
c = Canvas(root,bg = "white",height = "500",width ="1000")
c.grid(row=2,column=4)

def plot_graph():
    data = load('data.npy')
    ca=np.array([[000,000,1,1],
             [000,000,1,.8],
             [00,00,1,.7],
             [000,.5,00,1],
             [000,.5,000,.8],
             [000,.5,000,.7],
             [1,1,000,1],
             [1,1,000,.8],
             [1,1,000,.7],
             [1,000,000,1],
             [1,000,000,1],
             [1,000,000,1]])
    channel=[0.000,.0010,.0050,.0080,.010,.070,.1,.3,.5,.7,.8,1]
    cmap = matplotlib.colors.ListedColormap(ca)
#channel=[1,.8,.7,.5,.3,.1,.05,.010,.0080,.0050,.0010,.0001]
    norm = matplotlib.colors.BoundaryNorm(channel, len(ca))
    plt.ion() # Ensure that redrawing is possible
    fig,ax = plt.subplots()
    im = ax.imshow(data.reshape((int(p1),int(p2))).T, cmap=cmap,norm=norm)
    plt.imshow(v, cmap=cmap, norm=norm)
    cb = plt.colorbar(ticks=np.arange(len(ca)))
    cb.ax.set_yticklabels(np.unique(ca[:,0]))
    fig.show()
    im.set_array(data.reshape((int(p1),int(p2))).T)

    def plot(): 
      
      
        # creating the Tkinter canvas 
        # containing the Matplotlib figure 
        canvas = FigureCanvasTkAgg(fig, 
                                   master =newWindow2)   
        canvas.draw() 
      
        # placing the canvas on the Tkinter window 
        canvas.get_tk_widget().pack() 
      
        # creating the Matplotlib toolbar 
        toolbar = NavigationToolbar2Tk(canvas, 
                                       newWindow2) 
        toolbar.update() 
    # placing the toolbar on the Tkinter window 
        canvas.get_tk_widget().pack()

    newWindow2 = tk.Toplevel(root)
    plot_button = Button(master =newWindow2, 
					command = plot, 
					height = 2, 
					width = 10, 
					text = "Plot") 

    # place the button 
    # in main window 
    plot_button.pack() 
    # Progress bar widget
def progress1():
    newWindow1 = tk.Toplevel(root)
    global progress
    progress = Progressbar(newWindow1, orient =HORIZONTAL, 
                  length = 100, mode = 'determinate')
    def bar():
        progress['value'] = 20
        root.update_idletasks() 
        time.sleep(1)
        #load_array=[[['100'], [200, 1]],[['100'], [200, 1]]]
        lod=load2.load1(int(p1),int(p2),load_array)
        bound=BC.fixed(int(p1),int(p2))
        test_truss.run(int(p1),int(p2),lod,bound)
        progress['value'] = 40
        root.update_idletasks() 
        time.sleep(1) 
      
        progress['value'] = 50
        root.update_idletasks() 
        time.sleep(1) 
      
        progress['value'] = 60
        root.update_idletasks() 
        time.sleep(1) 
      
        progress['value'] = 80
        root.update_idletasks() 
        time.sleep(1) 
        progress['value'] = 100  
        progress.pack(pady = 10)
    progress.pack(pady = 10)
    Button(newWindow1, text = 'Start', command = bar).pack(pady = 10) 
def motion(event):
    x, y = event.x, event.y
    print('{}, {}'.format(x, y))
    X.append(x)
    Y.append(y)

#root.bind('<Motion>', motion)

def delete():
    c.delete("all")
    
def mouse_click(event):
    '''  delay mouse action to allow for double click to occur
    '''
    c.after(300, mouse_action, event)

def double_click(event):
    '''  set the double click status flag
    '''
    global double_click_flag
    double_click_flag = True

def mouse_action(event):
    global double_click_flag
    if double_click_flag:
        print('double mouse click')
        root.bind('<Motion>', motion)
        global r1,r2
        r1=X.pop()
        rec.append(r1)
        r2=Y.pop()
        rec.append(r2)
        print(r1,r2,rec)
        c.create_oval(r1-2,r2-2,r1+2,r2+2, outline="red",
                fill="red", width=1)
        double_click_flag = False
    else:
        print('single mouse click event')

def draw():
    #double_click_flag = False
    c.bind('<Button-1>', mouse_click) # bind left mouse click
    c.bind('<Double-1>', double_click)
    
def circle_create():
    global circle_point
    circle_point=circle.get()
    c.create_oval(r1-int(circle_point),r2-int(circle_point),r1+int(circle_point),r2+int(circle_point), outline="black",
                fill="white", width=1)
    print("First Name: %s\nLast Name: %s" % (p1,p2))
   
def circle_data():
    newWindow = tk.Toplevel(root)
    labelExample = tk.Label(newWindow, text = "Enter circle redius value")
   
    tk.Label(newWindow , 
         text="circle redius").grid(row=0)
    draw()
    global circle
    circle= tk.Entry(newWindow )
    circle.grid(row=0, column=1)
    tk.Button(newWindow , 
              text='Quit', 
              command=newWindow.destroy).grid(row=3, 
                                        column=0, 
                                        sticky=tk.W, 
                                        pady=4)
    tk.Button(newWindow, 
              text='Show', command=circle_create).grid(row=3, 
                                                           column=1, 
                                                           sticky=tk.W, 
                                                         pady=4)
def rectangle_create():
    global p1,p2
    p1=e1.get()
    p2=e2.get()
    c.create_rectangle(0,0,int(p1)+0, int(p2)+0,
                outline="dim gray", fill="dim gray", width=2)
    print("First Name: %s\nLast Name: %s" % (p1,p2))
   
def rectangle_data():
    newWindow = tk.Toplevel(root)
    labelExample = tk.Label(newWindow, text = "Enter rectangle value")
   
    tk.Label(newWindow , 
         text="Length").grid(row=0)
    tk.Label(newWindow , 
             text="Breadth").grid(row=1)
    global e1,e2
    e1 = tk.Entry(newWindow )
    e2 = tk.Entry(newWindow )
    e1.grid(row=0, column=1)
    e2.grid(row=1, column=1)
    tk.Button(newWindow , 
              text='Quit', 
              command=newWindow.destroy).grid(row=3, 
                                        column=0, 
                                        sticky=tk.W, 
                                        pady=4)
    tk.Button(newWindow, 
              text='Show', command=rectangle_create).grid(row=3, 
                                                           column=1, 
                                                           sticky=tk.W, 
                                                         pady=4)
def box_create():
    global q1,q2
    q1=b1.get()
    q2=b2.get()
    c.create_rectangle(r1,r2,int(q1)+r1, int(q2)+r2,
                outline="white", fill="white", width=2)
    print("First Name: %s\nLast Name: %s" % (p1,p2))
   
def box_data():
    newWindow = tk.Toplevel(root)
    labelExample = tk.Label(newWindow, text = "Enter box value")
   
    tk.Label(newWindow , 
         text="Length").grid(row=0)
    tk.Label(newWindow , 
             text="Breadth").grid(row=1)
    draw()
    global b1,b2
    b1= tk.Entry(newWindow )
    b2= tk.Entry(newWindow )
    b1.grid(row=0, column=1)
    b2.grid(row=1, column=1)
    tk.Button(newWindow , 
              text='Quit', 
              command=newWindow.destroy).grid(row=3, 
                                        column=0, 
                                        sticky=tk.W, 
                                        pady=4)
    tk.Button(newWindow, 
              text='Show', command=box_create).grid(row=3, 
                                                           column=1, 
                                                           sticky=tk.W, 
                                                         pady=4)
def Load():
    global load_point
    load_point=load1.get()
    load_array.append([[load_point],[r1,r2]])
    #l.load1()
    print("First Name:",load_array)
   
def Load_data():
    global load_array
    load_array=[]
    newWindow = tk.Toplevel(root)
    labelExample = tk.Label(newWindow, text = "Enter circle redius value")
   
    tk.Label(newWindow , 
         text="Load Value").grid(row=0)
    draw()
    global load1
    load1= tk.Entry(newWindow )
    load1.grid(row=0, column=1)
    tk.Button(newWindow , 
              text='Quit', 
              command=newWindow.destroy).grid(row=3, 
                                        column=0, 
                                        sticky=tk.W, 
                                        pady=4)
    tk.Button(newWindow, 
              text='Add', command=Load).grid(row=3,column=1, 
                                                      sticky=tk.W, 
                                                     pady=4)
    
new = 1
url = "https://www.google.com"
def openweb():
    webbrowser.open(url,new=new)

def rectangle():
    rectangle_data()
def circle1():
    circle_data()
def box():
    box_data()
def loads():
    Load_data()
button1 = tk.Button(root, 
                   text="rectangle", 
                   fg="red",
                   command=rectangle)
button2 = tk.Button(root, 
                   text="Delete", 
                   fg="red",
                   command=delete)
button1.grid(row=1,column=1)
button2.grid(row=2, column=1)

#button1.pack(side=tk.LEFT)
button3 = tk.Button(root,
                   text="circle",
                   command=circle1)
button3.grid(row=3,column=1,padx=5,pady=5)
button4= tk.Button(root,
                   text="Box",
                   command=box)
button5 = tk.Button(root,
                   text="Line",
                   command=draw)
button4.grid(row=3,column=2,padx=5,pady=5)
button5.grid(row=3,column=3,padx=5,pady=5)

button6 = tk.Button(root,
                   text="Load",bg="black",fg="white",
                   command=loads)
button7 = tk.Button(root,
                   text="Boundary",
                   command=draw)
button8 = tk.Button(root,
                   text="Simulation",
                   command=progress1)
button9 = tk.Button(root,
                   text="Result",
                   command=plot_graph)
button10 = tk.Button(root,
                   text="Aboutus",
                   command=openweb)
button11 = tk.Button(root,
                   text="Point",
                   command=draw)
button6.grid(row=1,column=2,padx=10,pady=10)
button7.grid(row=1,column=3,padx=10,pady=10)
button8.grid(row=1,column=4,padx=10,pady=10)
button9.grid(row=1,column=5,padx=10,pady=10)
button10.grid(row=1,column=6,padx=10,pady=10)
button11.grid(row=3,column=4,padx=5,pady=5)
double_click_flag = False
root.mainloop()







