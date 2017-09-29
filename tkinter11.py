from tkinter import*

def do_this():
	print("shantanu shukla")


root = Tk()

###### creating Menu #######

menu = Menu(root)
root.config(menu = menu)

#### creating sub menu and including cascading to first submenu ######

submenu = Menu(menu)
menu.add_cascade(label="File", menu=submenu)


#### adding submenu(file) content #####

submenu.add_command(label="add new project", command=do_this)
submenu.add_command(label="save it", command=do_this)
submenu.add_separator()   #for ... in last to seperate
submenu.add_command(label="Exit", command=do_this)


##### creating another submenu ###

editmenu = Menu(menu)
menu.add_cascade(label="Edit", menu=editmenu)


#### adding submenu(editmenu) content #####

editmenu.add_command(label = "edit it", command = do_this)

######### TOOLBAR ###########

toolbar = Frame(root, bg= "green")

tool_button = Button(toolbar, text = "upload", command = do_this)
tool_button.pack(side = LEFT, padx = 2, pady = 2)   #padx and pady are space pixel 

print_button = Button(toolbar, text = "print", command = do_this)
print_button.pack(side = LEFT, padx = 2, pady = 2)

toolbar.pack(side = TOP, fill = X)


####### STATUSBAR #########

status = Label(root, text = "nothing is showing...", bd = 1,relief = SUNKEN, anchor = W) # bd->how thick border line, sunken->streching won't effect text size,W->print west side
status.pack(side = BOTTOM, fill = X)




root.mainloop()


 
