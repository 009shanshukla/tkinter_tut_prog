from tkinter import*

root = Tk()    #constructor to create tkinter object(root) ,just think a blank window
start_label = Label(root, text="This is easy") #giving it a name 
start_label.pack()     #pack everything above object
root.mainloop()  #run GUI infinitely untill user won't close it
