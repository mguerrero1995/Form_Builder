import tkinter as tk
from tkinter import ttk

# Define the size of the grid
# NUM_ROWS = 12
# NUM_COLS = 12

window = tk.Tk()
window.geometry("800x800")

class DraggableWidget:
    next_id = 1
    all_instances = []

    def __init__(self, name, type, widget_width=10, widget_height=5):
        self.id = DraggableWidget.next_id
        self.name = name
        # self.initial_x = initial_x
        # self.initial_y = initial_y
        self.widget_width = widget_width
        self.widget_height = widget_height
        type = type.upper()
        # self.location = {"top_left": [self.initial_x, self.initial_y], 
        #                 "top_right": [self.initial_x + self.widget_width],
        #                 "bottom_left": [self.initial_x, self.initial_y + 100],
        #                 "bottom_right": [self.initial_x + self.widget_width, self.initial_y + self.widget_height],
        #                 "left_x": self.initial_x,
        #                 "right_x": self.initial_x + self.widget_width,
        #                 "top_y": self.initial_y,
        #                 "bottom_y": self.initial_y + self.widget_height}

        if type == "LABEL":
            self.field = tk.Label(window, text=self.name, bg="red", # width=4, height=2,
                bd=1, relief=tk.SOLID, highlightthickness=1, highlightbackground="black")
            self.field.pack(padx=1, pady=1)
        elif type == "ENTRY":
            self.field = tk.Entry(window, bg="red", # width=4, height=2,
                bd=1, relief=tk.SOLID, highlightthickness=1, highlightbackground="black")
            self.field.insert(0, self.name)
            self.field.pack(padx=1, pady=1)
        elif type == "BUTTON":
            self.field = tk.Button(window, text=self.name, bg="red", # width=4, height=2,
                bd=1, relief=tk.SOLID, highlightthickness=1, highlightbackground="black")
            self.field.pack(padx=1, pady=1)
        else:
            raise ValueError("Invalid field type")

        DraggableWidget.all_instances.append(self)
        
        self.add_widget()

        self.location = {"top_left": [self.field.winfo_x(), self.field.winfo_y()], 
                        "top_right": [self.field.winfo_x() + self.widget_width],
                        "bottom_left": [self.field.winfo_x(), self.field.winfo_y() + 100],
                        "bottom_right": [self.field.winfo_x() + self.widget_width, self.field.winfo_y() + self.widget_height],
                        "left_x": self.field.winfo_x(),
                        "right_x": self.field.winfo_x() + self.widget_width,
                        "top_y": self.field.winfo_y(),
                        "bottom_y": self.field.winfo_y() + self.widget_height}
        
        # self.bind_drag()
        # DraggableWidget.next_id += 1



    # Bind events to the label
    def on_button_press(self, event):
        widget = event.widget
        widget.lift()
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

        self.location["left_x"] = x
        self.location["right_x"] = x + self.widget_width
        self.location["top_y"] = y 
        self.location["bottom_y"] = y + self.widget_height
        
        # Set the position of the label in the window
        widget.place(x=x, y=y)

        self.check_edge_alignment()
            
    def on_button_release(self, event):
        widget = event.widget
        x = widget.winfo_x()
        y = widget.winfo_y()

        widget.place(x=x, y=y)

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
    
    def check_edge_alignment(self):
        other_widgets = [instance for instance in DraggableWidget.all_instances if instance != self]
        # print(other_widgets)

        canvas = None
         
        for other_widget in other_widgets:
            if self.location["left_x"] == other_widget.location["left_x"]:
                # Move the canvas to the appropriate location
                canvas = tk.Canvas(window, width=1, height=window.winfo_height(), bg="black", highlightthickness=0)
                canvas.place(x=self.location["left_x"], y=0)
            elif self.location["right_x"] == other_widget.location["right_x"]:
                # Move the canvas to the appropriate location
                canvas = tk.Canvas(window, width=1, height=window.winfo_height(), bg="black", highlightthickness=0)
                canvas.place(x=self.location["right_x"] + self.widget_width, y=0)
            elif self.location["top_y"] == other_widget.location["top_y"]:
                # Move the canvas to the appropriate location
                canvas = tk.Canvas(window, width=1, height=window.winfo_height(), bg="black", highlightthickness=0)
                canvas.place(x=0, y=self.location["top_y"])
            elif self.location["bottom_y"] == other_widget.location["bottom_y"]:
                # Move the canvas to the appropriate location
                canvas = tk.Canvas(window, width=1, height=window.winfo_height(), bg="black", highlightthickness=0)
                canvas.place(x=0, y=self.location["bottom_y"] + self.widget_height)
            else:
                # Hide the canvas when the edges do not align
                if canvas:
                    canvas.place_forget()

        # for other_widget in DraggableWidget.all_instances:
        #     if other_widget.id == self.id:
        #         continue
            
        #     for location in self.location:


        #     for location in self.location:
        #         for other_location in other_widget.location:
        #             if location == other_location:
        #                 continue

        #             self_coord = self.location[location]
        #             other_coord = other_widget.location[other_location]

        #             if abs(self_coord[0] - other_coord[0]) <= 2:
        #                 # Draw a vertical line through the window at the relevant x value
        #                 x = self_coord[0]
        #                 canvas = tk.Canvas(window, width=1, height=window.winfo_height(), bg="black", highlightthickness=0)
        #                 canvas.place(x=x, y=0)

        #             if abs(self_coord[1] - other_coord[1]) <= 2:
        #                 # Draw a horizontal line through the window at the relevant y value
        #                 y = self_coord[1]
        #                 canvas = tk.Canvas(window, width=window.winfo_width(), height=1, bg="black", highlightthickness=0)
        #                 canvas.place(x=0, y=y)


    # def bind_drag(self):
    #     self.field.bind("<ButtonPress-1>", func=self.on_button_press)
    #     self.field.bind("<ButtonRelease-1>", func=self.on_button_release)
    #     self.field.bind("<B1-Motion>", func=self.on_button_motion)
    
    def add_widget(self):
        self.field.bind("<ButtonPress-1>", func=self.on_button_press)
        self.field.bind("<ButtonRelease-1>", func=self.on_button_release)
        self.field.bind("<B1-Motion>", func=self.on_button_motion)
        self.field.bind("<Enter>", self.on_enter)
        self.field.bind("<Leave>", self.on_leave)
        
        DraggableWidget.next_id += 1




label1 = DraggableWidget(name="Label 1", type="label")
label2 = DraggableWidget(name="Label 2", type="label")

button1 = DraggableWidget(name="Button 1", type="button")
button2 = DraggableWidget(name="Button 2", type="button")

# Create a label to move around the grid
# label1 = DraggableWidget(window, text="Label 1", bg="red", width=4, height=2,
#                   bd=1, relief=tk.SOLID, highlightthickness=1, highlightbackground="black")

# label2 = DraggableWidget(window, text="Label 2", bg="blue", width=4, height=2,
#                   bd=1, relief=tk.SOLID, highlightthickness=1, highlightbackground="black")

# Set the initial position of the label

window.mainloop()