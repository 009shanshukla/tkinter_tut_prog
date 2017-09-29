from tkinter import*

root = Tk()    #constructor to create tkinter object(root) ,just think a blank window

top_frame = Frame(root)     #first frame
top_frame.pack()          #pack it on top by default
bottom_frame = Frame(root)    #second frame
bottom_frame.pack(side = BOTTOM)      #pack it on left ,argument side decides


button1 = Button(top_frame, text="first", fg="red") 
button2 = Button(top_frame, text="second", fg="green")
button3 = Button(top_frame, text="third", fg="purple")
button4 = Button(bottom_frame, text="fourth", fg="blue")

button1.pack(side=LEFT)            #pack it as much left as possible  otherwise it will show on top of each other
button2.pack(side=LEFT)
button3.pack(side=LEFT)
button4.pack()

root.mainloop()  #run GUI infinitely untill user won't close it
