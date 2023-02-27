import tkinter as tk
from tkinter import ttk

# Define the size of the grid
# NUM_ROWS = 12
# NUM_COLS = 12

window = tk.Tk()
window.geometry("800x800")

class DraggableWidget:
    next_id = 1

    def __init__(self, name, type, widget_width=10, widget_height=5, initial_x=0, initial_y=0):
        self.id = DraggableWidget.next_id
        self.name = name
        # self.initial_row = initial_row
        # self.initial_col = initial_col
        # self.width = 100
        # self.height = 30
        self.initial_x = initial_x
        self.initial_y = initial_y
        self.widget_width = widget_width
        self.widget_height = widget_height
        type = type.upper()
        self.location = {"top_left": [self.initial_x, self.initial_y], 
                        "top_right": [self.initial_x + self.widget_width],
                        "bottom_left": [self.initial_x, self.initial_y + 100],
                        "bottom_right": [self.initial_x + self.widget_width, self.initial_y + self.widget_height]}

        if type == "LABEL":
            self.field = tk.Label(window, text=self.name, bg="red", # width=4, height=2,
                bd=1, relief=tk.SOLID, highlightthickness=1, highlightbackground="black")
            
        elif type == "ENTRY":
            self.field = tk.Entry(window, bg="red", # width=4, height=2,
                bd=1, relief=tk.SOLID, highlightthickness=1, highlightbackground="black")
            self.field.insert(0, self.name)
        elif type == "BUTTON":
            self.field = tk.Button(window, text=self.name, bg="red", # width=4, height=2,
                bd=1, relief=tk.SOLID, highlightthickness=1, highlightbackground="black")
        else:
            raise ValueError("Invalid field type")

        # Place the field in it's inital location
        # self.field.place(row=self.initial_row, column=self.initial_col, padx=1, pady=1)
        self.field.pack(padx=1, pady=1)

        self.bind_drag()
        DraggableWidget.next_id += 1

        self.field.bind("<Enter>", self.on_enter)
        self.field.bind("<Leave>", self.on_leave)

    # Bind events to the label
    def on_button_press(self, event):
        widget = event.widget
        # print(widget.winfo_width(), widget.winfo_height())
        # Remember the initial position of the label and the mouse
        widget.startX = event.x
        widget.startY = event.y

    def on_button_motion(self, event):
        widget = event.widget

        # Calculate the new position of the label based on the mouse movement
        x = widget.winfo_x() - widget.startX + event.x
        y = widget.winfo_y() - widget.startY + event.y

        self.location["upper_left"] = [x, y]
        self.location["upper_right"] = [x + self.widget_width, y]
        self.location["bottom_left"] = [x, y + self.widget_height]
        self.location["bottom_right"] = [x + self.widget_width, y + self.widget_height]
        
        # Set the position of the label in the window
        widget.place(x=x, y=y)
        # Add print here
        
    def on_button_release(self, event):
        # Snap the label to the nearest grid position
        widget = event.widget
        x = widget.winfo_x()
        y = widget.winfo_y()

        widget.place(x=x, y=y)


        # row = int((y + widget.winfo_height() // 2) / widget.winfo_reqheight())
        # col = int((x + widget.winfo_width() // 2) / widget.winfo_reqwidth())
        # row = max(0, min(row, NUM_ROWS - 1))
        # col = max(0, min(col, NUM_COLS - 1))

        # Update the label position with the grid coordinates
        # widget.place(x=col * widget.winfo_reqwidth(), y=row * widget.winfo_reqheight())

    def on_enter(self, event):
        widget = event.widget
        x, y = event.x, event.y
        w = widget.winfo_width()
        h = widget.winfo_height()

        if x <= 2 or y <= 2 or x >= w - 2 or y >= h - 2:
            widget.config(cursor="sizing")
        
    def on_leave(self, event):
        widget = event.widget
        x, y = event.x, event.y
        w = widget.winfo_width()
        h = widget.winfo_height()
        
        if x > 2 or y > 2 or x < w - 2 or y < h - 2:
            widget.config(cursor="arrow")

    def bind_drag(self):
        self.field.bind("<ButtonPress-1>", func=self.on_button_press)
        self.field.bind("<ButtonRelease-1>", func=self.on_button_release)
        self.field.bind("<B1-Motion>", func=self.on_button_motion)


        
        
        
        

label1 = DraggableWidget(name="Label 1", type="label", initial_x=0, initial_y=0)
label2 = DraggableWidget(name="Label 2", type="label", initial_x=0, initial_y=1)

button1 = DraggableWidget(name="Button 1", type="button", initial_x=0, initial_y=2)
button2 = DraggableWidget(name="Button 2", type="button", initial_x=0, initial_y=3)

# Create a label to move around the grid
# label1 = DraggableWidget(window, text="Label 1", bg="red", width=4, height=2,
#                   bd=1, relief=tk.SOLID, highlightthickness=1, highlightbackground="black")

# label2 = DraggableWidget(window, text="Label 2", bg="blue", width=4, height=2,
#                   bd=1, relief=tk.SOLID, highlightthickness=1, highlightbackground="black")

# Set the initial position of the label

window.mainloop()