import tkinter as tk
window = tk.Tk()
window.title('my window')
window.geometry('400x400')
def moveup():
    canvas.move(image,0,-4)
def movedown():
    canvas.move(image,0,4)
def moveleft():
    canvas.move(image,-4,0)
def moveright():
    canvas.move(image,4,0)
canvas = tk.Canvas(window,bg = 'green',height = 200,width = 300)
image_loading = tk.PhotoImage(file = '1.gif')
image = canvas.create_image(10,10,anchor = 'nw',
                            image = image_loading)

x=50
y=50
x1=80
y1=80
line = canvas.create_line(x,y,x1,y1)
canvas.pack()
b1 = tk.Button(window,text = '向上',command = moveup)
b1.pack()
b2 = tk.Button(window,text = '向下',command = movedown)
b2.pack()
b3 = tk.Button(window,text = '向左',command = moveleft)
b3.pack()
b4 = tk.Button(window,text = '向右',command = moveright)
b4.pack()
window.mainloop()