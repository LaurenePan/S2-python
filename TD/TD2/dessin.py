import tkinter as tk 

CANVAS_WIDTH, CANVAS_HEIGHT = 600, 600

tk.root = tk.Tk()

tk.canvas = tk.Canvas(tk.root, width = CANVAS_WIDTH, height = CANVAS_HEIGHT)

tk.canvas.grid(row=4,column=2)

tk.root.title("Mon Dessin")

tk.canvas2 = tk.Canvas(tk.root, bg="red", height=100, width=100)

tk.canvas2.mainloop()

tk.root.mainloop()

