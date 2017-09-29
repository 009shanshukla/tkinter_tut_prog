from tkinter import*

root = Tk()

########### mouse keys event defined ######

def left_click(event):
	print("left")

def middle_click(event):
	print("middle")

def right_click(event):
	print("right")

######## binding with a frame #####
##### button-1 is left button in mouse and respectively 

frame = Frame(root,width = 600, height = 600)
frame.bind("<Button-1>",left_click)
frame.bind("<Button-2>",middle_click)
frame.bind("<Button-3>",right_click)


root.mainloop()
