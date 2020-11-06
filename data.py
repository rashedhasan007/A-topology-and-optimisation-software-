import tkinter as tk

def show_entry_fields():
    global p1,p2
    p1=e1.get()
    p2=e2.get()
    array.append(p1)
    array.append(p2)
    print("First Name: %s\nLast Name: %s" % (p1,p2))
   
def rectangle_data():
    newWindow = tk.Toplevel(app)
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
              text='Show', command=show_entry_fields).grid(row=3, 
                                                           column=1, 
                                                           sticky=tk.W, 
                                                         pady=4)

    
   
#app = tk.Tk()
#buttonExample = tk.Button(app, 
             # text="Create new window",
              #command=rectangle_data)
#buttonExample.pack()

#app.mainloop()