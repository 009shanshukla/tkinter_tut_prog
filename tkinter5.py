from tkinter import*

root = Tk()

######making label #######

label1 = Label(root, text="name")
label2 = Label(root, text="password")

### for entry in label #########

entry1 = Entry(root)
entry2 = Entry(root)

######### positioning label and entry ######

label1.grid(row=0, sticky=E)        # second argument stands for E->East aligned
label2.grid(row=1,sticky=E)
entry1.grid(row=0,column=1)
entry2.grid(row=1,column=1)

########check button ######

c = Checkbutton(root, text="keep me logged in")
c.grid(columnspan=2) #gonna take two column



root.mainloop()
