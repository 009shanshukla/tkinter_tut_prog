from tkinter import*

root = Tk()

canvas = Canvas(root, width = 600, height = 600)
canvas.pack()

black = canvas.create_line(0,0,100,150)
green = canvas.create_line(550,550,200,400, fill = "green")

rectangle = canvas.create_rectangle(300,300,400,400,fill = "red")
#canvas.delete(green)


root.mainloop()
