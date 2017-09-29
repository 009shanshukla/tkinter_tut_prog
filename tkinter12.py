from tkinter import*
import tkinter.messagebox

root = Tk()

tkinter.messagebox.showinfo('window title','windows is shutting down')

answer = tkinter.messagebox.askquestion('question 1-','do you like pizza ?')

if answer == 'yes':
	print(")()()()(")


root.mainloop()
