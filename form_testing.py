import tkinter as tk
from tkinter import ttk

# Define the size of the grid
NUM_ROWS = 12
NUM_COLS = 12

window = tk.Tk()



# Create a grid layout with empty labels to define the size of the grid
for row in range(NUM_ROWS):
    for col in range(NUM_COLS):
        label = tk.Label(window, text="", width=4, height=2, bd=1, relief=tk.SOLID,
                         highlightthickness=1, highlightbackground="black")
        label.grid(row=row, column=col, padx=2, pady=2)
        # if row < 2 or row > 11 or col < 2 or col > 11:
        #     # Make the empty cells invisible
        #     label.grid_remove()



class DraggableWidget:
    next_id = 1

    def __init__(self, name, type, initial_x, initial_y):
        self.id = DraggableWidget.next_id
        self.name = name
        self.initial_x = initial_x
        self.initial_y = initial_y
        self.width = 100
        self.height = 30
        type = type.upper()

        if type == "LABEL":
            self.field = tk.Label(window, text=self.name, bg="red", width=4, height=2,
                bd=1, relief=tk.SOLID, highlightthickness=1, highlightbackground="black")
            
        elif type == "ENTRY":
            self.field = tk.Entry(window, bg="red", width=4, height=2,
                bd=1, relief=tk.SOLID, highlightthickness=1, highlightbackground="black")
            self.field.insert(0, self.name)
        elif type == "BUTTON":
            self.field = tk.Button(window, text=self.name, bg="red", width=4, height=2,
                bd=1, relief=tk.SOLID, highlightthickness=1, highlightbackground="black")
        else:
            raise ValueError("Invalid field type")

        # Place the field in it's inital location
        self.field.place(x=self.initial_x, y=self.initial_y)

        self.bind_drag()
        DraggableWidget.next_id += 1

    # Bind events to the label
    def on_button_press(self, event):
        widget = event.widget
        print(widget.winfo_width(), widget.winfo_height())
        # Remember the initial position of the label and the mouse
        widget.startX = event.x
        widget.startY = event.y

    def on_button_motion(self, event):
        widget = event.widget

        # Calculate the new position of the label based on the mouse movement
        x = widget.winfo_x() - widget.startX + event.x
        y = widget.winfo_y() - widget.startY + event.y
        
        # Set the position of the label in the window
        widget.place(x=x, y=y)

    def on_button_release(self, event):
        # Snap the label to the nearest grid position
        widget = event.widget
        x = widget.winfo_x()
        y = widget.winfo_y()
        row = int((y + widget.winfo_height() // 2) / widget.winfo_reqheight())
        col = int((x + widget.winfo_width() // 2) / widget.winfo_reqwidth())
        row = max(0, min(row, NUM_ROWS - 1))
        col = max(0, min(col, NUM_COLS - 1))

        # Update the label position with the grid coordinates
        widget.place(x=col * widget.winfo_reqwidth(), y=row * widget.winfo_reqheight())

    def bind_drag(self):
        self.field.bind("<ButtonPress-1>", func=self.on_button_press)
        self.field.bind("<ButtonRelease-1>", func=self.on_button_release)
        self.field.bind("<B1-Motion>", func=self.on_button_motion)


        
        
        
        

label1 = DraggableWidget("Label 1", "label", 0, 0)
label2 = DraggableWidget("Label 2", "label", 0, 35)

button1 = DraggableWidget("Button 1", "button", 0, 70)
button2 = DraggableWidget("Button 2", "button", 0, 105)

# Create a label to move around the grid
# label1 = DraggableWidget(window, text="Label 1", bg="red", width=4, height=2,
#                   bd=1, relief=tk.SOLID, highlightthickness=1, highlightbackground="black")

# label2 = DraggableWidget(window, text="Label 2", bg="blue", width=4, height=2,
#                   bd=1, relief=tk.SOLID, highlightthickness=1, highlightbackground="black")

# Set the initial position of the label

window.mainloop()