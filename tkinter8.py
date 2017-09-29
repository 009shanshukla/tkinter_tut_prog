from tkinter import*


##########definig everythind inside class ######

class definition:
	def __init__(self,master): 
		frame = Frame(master)
		frame.pack()

		self.print_button = Button(frame, text="print msg", command = self.printmessage )
		self.print_button.pack(side = LEFT)

		self.quit_button = Button(frame, text="quit", command = frame.quit )      #frame.quit is in-built function
		self.quit_button.pack(side = LEFT)

	def printmessage(self):
		print("wow, gotchchchcaaa..")	


###### creating tkinter container and object for class #######
root = Tk()
obj = definition(root)

root.mainloop() 
