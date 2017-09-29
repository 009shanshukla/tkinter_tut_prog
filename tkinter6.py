from tkinter import*

root = Tk()

def myname(event):
	print("shantanu shukla")


####### binding function with GUI(widget) #####
button1 = Button(root, text="print name")
button1.bind("<Button-1>",myname)
button1.pack()



root.mainloop()
