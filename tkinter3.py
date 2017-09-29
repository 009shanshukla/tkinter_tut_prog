from tkinter import*

root = Tk()

######making lable #######

one = Label(root, text="one", bg="red", fg="white")        #bg stands for background color
one.pack()                #static label

two = Label(root, text="two", bg="green", fg="black")
two.pack(fill=X)   #label that streches in x-dir

three = Label(root, text="one", bg="red", fg="white")
three.pack(side=LEFT, fill=Y)    #label that streches in y-dir

root.mainloop()
