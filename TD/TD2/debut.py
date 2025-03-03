import tkinter as tk 

CANVAS_WIDTH, CANVAS_HEIGHT = 600, 600

tk.root = tk.Tk()

tk.canvas = tk.Canvas(tk.root, width = CANVAS_WIDTH, height = CANVAS_HEIGHT)

    # Début de votre code
x0 = CANVAS_WIDTH/2
y0=100
y1= CANVAS_HEIGHT-100
tk.canvas.create_line(x0, y0, x0, y1)
tk.canvas.create_oval(x0 - 50, y0 + 50, x0 + 50, y0 - 50)
tk.canvas.create_oval(x0 - 50, y1 + 50 , x0+50, y1-50)
tk.canvas.create_oval(x0+50 ,(y0 + y1) / 2 - 50 ,x0-50,(y0 + y1) / 2 + 50 )
    
    # Fin de votre code
tk.canvas.grid(row=0,column=0)
tk.root.mainloop()