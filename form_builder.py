import tkinter as tk
# from tkinter import ttk
import pandas as pd
from datetime import datetime
from sqlalchemy import create_engine


# Define parameters for querying SQL Server

server = "APP-P-RWHAAT.TEC.CLINITECH.NET" 
database = "RiskAdjustmentSandbox"
driver = "ODBC Driver 17 for SQL Server" # Pick your database driver
cnxn_str = f"mssql://@{server}/{database}?driver={driver}" # Builds the connection string to initialize the DB engine

# Create the engine
engine = create_engine(cnxn_str)
cnxn = engine.connect()



class NavigationButton(tk.Button):
    def __init__(self, parent, text, target_frame, controller, row, column):
        tk.Button.__init__(self, parent, text=text, command=lambda: controller.show_frame(target_frame))
        self.grid(row=row, column=column)


class EnterDataPage(tk.Frame):

    tbl_name = "DataEntryTest"
    tbl_schema = "dbo"

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # self.title("Data Entry Form")
        # self.geometry("500x500")     
        
        # tk.Label(self, text="Enter Data", font=("Helvetica", 14))
        # tk.grid(row=0, column=0)

        NavigationButton(parent=self, text="New Records", target_frame=EnterDataPage, controller=controller, row=6, column=4)
        NavigationButton(parent=self, text="Update Records", target_frame=UpdateDataPage, controller=controller, row=6, column=5)

        # tk.Label(self, text="Create ID").pack()
        # tk.Entry(self).pack()

        self.form_header = "Data Entry Form"
        
        # This is the title inside of the window
        self.form_header_lab = tk.Label(self, text=self.form_header)
        self.form_header_lab.grid(row=0, column=0, padx=10, pady=10, columnspan=4)


        self.fn_lab = tk.Label(self, text="First Name")
        self.fn_lab.grid(row=1, column=0, padx=5, pady=5)
        self.fn_entry = tk.Entry(self)
        self.fn_entry.grid(row=1, column=1, columnspan=3)



        self.ln_lab = tk.Label(self, text="Last Name")
        self.ln_lab.grid(row=2, column=0, padx=5, pady=5)

        self.ln_entry = tk.Entry(self)
        self.ln_entry.grid(row=2, column=1, columnspan=3)



        self.dob_lab = tk.Label(self, text="DOB")
        self.dob_lab.grid(row=4, column=0, padx=5, pady=5)



        self.dob_mm_lab = tk.Label(self, text="MM")
        self.dob_mm_lab.grid(row=3, column=1, padx=5, pady=5, sticky="w")
        self.dob_mm_entry = tk.Entry(self, width=2)
        self.dob_mm_entry.grid(row=4, column=1, ipadx=3, ipady=2, sticky="w")



        self.dob_dd_lab = tk.Label(self, text="DD")
        self.dob_dd_lab.grid(row=3, column=3, padx=5, pady=5, sticky="w")
        self.dob_dd_entry = tk.Entry(self, width=2)
        self.dob_dd_entry.grid(row=4, column=3, ipadx=3, ipady=2, sticky="w")



        self.dob_yyyy_lab = tk.Label(self, text="YYYY")
        self.dob_yyyy_lab.grid(row=3, column=5, padx=5, pady=5, sticky="w")
        self.dob_yyyy_entry = tk.Entry(self, width=4)
        self.dob_yyyy_entry.grid(row=4, column=5, ipadx=3, ipady=2, sticky="w")



        self.dob_mm_slash = tk.Label(self, text="/")
        self.dob_mm_slash.grid(row=4, column=2, padx=5, sticky="w")

        self.dob_dd_slash = tk.Label(self, text="/")
        self.dob_dd_slash.grid(row=4, column=4, padx=5, sticky="w")



        self.submit_btn = tk.Button(self, text="Submit New Record", command=self.on_submit)
        self.submit_btn.grid(row=5, column=0, padx=5, pady=10, columnspan=4)

    def on_submit(self):

        fn = self.fn_entry.get()
        ln = self.ln_entry.get()
        dob_yyyy = self.dob_yyyy_entry.get()
        dob_mm = self.dob_mm_entry.get()
        dob_dd = self.dob_dd_entry.get()

        df = pd.DataFrame([{"FirstName": fn, "LastName": ln, "DOB": f"{dob_yyyy}-{dob_mm}-{dob_dd}", "CreateTimestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")}])

class UpdateDataPage(tk.Frame):
    tbl_name = "DataEntryTest"
    tbl_schema = "dbo"

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # self.title("Data Entry Form")
        # self.geometry("500x500")     
        
        # tk.Label(self, text="Enter Data", font=("Helvetica", 14))
        # tk.grid(row=0, column=0)

        NavigationButton(parent=self, text="New Records", target_frame=EnterDataPage, controller=controller, row=6, column=4)
        NavigationButton(parent=self, text="Update Records", target_frame=UpdateDataPage, controller=controller, row=6, column=5)

        # tk.Label(self, text="Create ID").pack()
        # tk.Entry(self).pack()

        self.form_header = "Data Editing Form"
        
        # This is the title inside of the window
        self.form_header_lab = tk.Label(self, text=self.form_header)
        self.form_header_lab.grid(row=0, column=0, padx=10, pady=10, columnspan=4)


        self.fn_lab = tk.Label(self, text="First Name")
        self.fn_lab.grid(row=1, column=0, padx=5, pady=5)
        self.fn_entry = tk.Entry(self)
        self.fn_entry.grid(row=1, column=1, columnspan=3)



        self.ln_lab = tk.Label(self, text="Last Name")
        self.ln_lab.grid(row=2, column=0, padx=5, pady=5)

        self.ln_entry = tk.Entry(self)
        self.ln_entry.grid(row=2, column=1, columnspan=3)



        self.dob_lab = tk.Label(self, text="DOB")
        self.dob_lab.grid(row=4, column=0, padx=5, pady=5)



        self.dob_mm_lab = tk.Label(self, text="MM")
        self.dob_mm_lab.grid(row=3, column=1, padx=5, pady=5, sticky="w")
        self.dob_mm_entry = tk.Entry(self, width=2)
        self.dob_mm_entry.grid(row=4, column=1, ipadx=3, ipady=2, sticky="w")



        self.dob_dd_lab = tk.Label(self, text="DD")
        self.dob_dd_lab.grid(row=3, column=3, padx=5, pady=5, sticky="w")
        self.dob_dd_entry = tk.Entry(self, width=2)
        self.dob_dd_entry.grid(row=4, column=3, ipadx=3, ipady=2, sticky="w")



        self.dob_yyyy_lab = tk.Label(self, text="YYYY")
        self.dob_yyyy_lab.grid(row=3, column=5, padx=5, pady=5, sticky="w")
        self.dob_yyyy_entry = tk.Entry(self, width=4)
        self.dob_yyyy_entry.grid(row=4, column=5, ipadx=3, ipady=2, sticky="w")



        self.dob_mm_slash = tk.Label(self, text="/")
        self.dob_mm_slash.grid(row=4, column=2, padx=5, sticky="w")

        self.dob_dd_slash = tk.Label(self, text="/")
        self.dob_dd_slash.grid(row=4, column=4, padx=5, sticky="w")



        self.submit_btn = tk.Button(self, text="Submit Edits", command=self.on_submit)
        self.submit_btn.grid(row=5, column=0, padx=5, pady=10, columnspan=4)

    def on_submit(self):

        fn = self.fn_entry.get()
        ln = self.ln_entry.get()
        dob_yyyy = self.dob_yyyy_entry.get()
        dob_mm = self.dob_mm_entry.get()
        dob_dd = self.dob_dd_entry.get()

        df = pd.DataFrame([{"FirstName": fn, "LastName": ln, "DOB": f"{dob_yyyy}-{dob_mm}-{dob_dd}", "CreateTimestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")}])


class Application(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.title("Data Entry Application")
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (EnterDataPage, UpdateDataPage):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(EnterDataPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


if __name__ == "__main__":
    app = Application()
    app.mainloop()

