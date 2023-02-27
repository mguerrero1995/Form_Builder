import tkinter as tk
import tkinter.dnd as dnd
# from tkinter import ttk

window = tk.Tk()
window.title("Grid App")
window.geometry("750x750")

GRID_SIZE = 50

# set the default number of rows and columns
for i in range(15):
    window.grid_rowconfigure(i, minsize=20)
    window.grid_columnconfigure(i, minsize=20)

class DraggableField:
    next_id = 1

    def __init__(self, name, type, x, y):
        self.id = DraggableField.next_id
        self.canvas = tk.Canvas(window)
        self.canvas.pack(fill=tk.BOTH, expand=True)
        self.name = name
        self.x = x
        self.y = y
        self.width = 100
        self.height = 30
        type = type.upper()

        if type == "LABEL":
            self.field = tk.Label(self.canvas, text=self.name)
        elif type == "ENTRY":
            self.field = tk.Entry(self.canvas)
            self.field.insert(0, self.name)
        elif type == "BUTTON":
            self.field = tk.Button(self.canvas, text=self.name)
        else:
            raise ValueError("Invalid field type")

        self.field.grid(row=self.y, column=self.x, sticky="nw")
        self.bind_drag()
        DraggableField.next_id += 1

        self.drag_data = {"x": 0, "y": 0, "item": self.field, "x0": 0, "y0": 0}
    
    def start_drag(self, event):
        print(event, self.field)
        x, y = self.canvas.coords(self.field)
        self.drag_data = {"x": event.x, "y": event.y, "item": self.field, "x0": x, "y0": y}
    
    def drag(self, event):
        print(event)
        x, y = event.x - self.drag_data["x"], event.y - self.drag_data["y"]
        print(x, y)
        self.field.grid_forget()
        self.canvas.move(self.field, x, y)
        self.drag_data["x"], self.drag_data["y"] = event.x, event.y
    
    def end_drag(self, event):
        print(event)
        x, y = event.x, event.y
        x_index = int((self.canvas.winfo_pointerx() - self.canvas.winfo_rootx()) / GRID_SIZE)
        y_index = int((self.canvas.winfo_pointery() - self.canvas.winfo_rooty()) / GRID_SIZE)
        try:
            self.field.grid(row=y_index, column=x_index, sticky="nw")
        except tk.TclError:
            self.field.grid(row=self.y, column=self.x, sticky="nw")
    
    def bind_drag(self):
        self.field.bind("<Button-1>", self.start_drag)
        self.field.bind("<B1-Motion>", self.drag)
        self.field.bind("<ButtonRelease-1>", self.end_drag)


label = DraggableField("Label", "Label", 0, 0)
entry = DraggableField("Entry", "Entry", 1, 0)
button = DraggableField("Button", "Button", 2, 0)


window.mainloop()
