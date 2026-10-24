
import tkinter as tk
from tkinter import ttk  #imports themed widgets and stuff

from converter import UNITS, convert_units  # imports conversion logic


class UnitConverterApp:  # defines the application window

    def __init__(self, root):
        self.root = root  # stores the main window
        self.root.title("Unit Converter")  # sets the window title
        self.root.geometry("440x360")  # sets the window size
        self.root.resizable(False, False)  # prevents resizing

        self.input_value = tk.StringVar()  # stores number input
        self.from_unit = tk.StringVar(value="Meters (m)")  # sets starting unit
        self.to_unit = tk.StringVar(value="Kilometers (km)")  # sets target unit
        self.output_value = tk.StringVar()  # stores conversion result

        self.create_widgets()  # builds the interface

    def create_widgets(self):  # creates interface elements
        main_frame = ttk.Frame(self.root, padding=20)  # creates main container
        main_frame.pack(fill="both", expand=True)  # fills the window

        ttk.Label(
            main_frame, text="Unit Converter", font=("Arial", 18, "bold")
        ).pack(pady=(0, 18))  # displays the heading

        ttk.Label(main_frame, text="Enter a number:").pack(anchor="w")  # labels input

        input_box = ttk.Entry(
            main_frame, textvariable=self.input_value
        )  # creates number input
        input_box.pack(fill="x", pady=(4, 12))  # places input box
        input_box.focus()  # focuses the input box

        ttk.Label(main_frame, text="Convert from:").pack(anchor="w")  # labels source

        self.from_dropdown = ttk.Combobox(
            main_frame,
            textvariable=self.from_unit,
            values=list(UNITS.keys()),
            state="readonly",
        )  # creates starting-unit dropdown
        self.from_dropdown.pack(fill="x", pady=(4, 12))  # places dropdown

        ttk.Label(main_frame, text="Convert to:").pack(anchor="w")  # labels target

        self.to_dropdown = ttk.Combobox(
            main_frame,
            textvariable=self.to_unit,
            values=list(UNITS.keys()),
            state="readonly",
        )  # creates target-unit dropdown
        self.to_dropdown.pack(fill="x", pady=(4, 12))  # places dropdown

        convert_button = ttk.Button(
            main_frame, text="Convert", command=self.perform_conversion
        )  # creates conversion button
        convert_button.pack(fill="x", pady=(4, 12))  # places button

        ttk.Label(main_frame, text="Result:").pack(anchor="w")  # labels output

        output_box = ttk.Entry(
            main_frame, textvariable=self.output_value, state="readonly"
        )  # creates read-only output box
        output_box.pack(fill="x", pady=(4, 0))  # places output box

        self.root.bind("<Return>", self.perform_conversion)  # converts on Enter

    def perform_conversion(self, event=None):  # handles conversion requests
        number = float(self.input_value.get())  # converts input text to a number

        result = convert_units(
            number, self.from_unit.get(), self.to_unit.get()
        )  # performs conversion

        self.output_value.set(f"{result:.10g}")  # displays formatted result

import tkinter as tk
from tkinter import ttk  #imports themed widgets and stuff

from converter import UNITS, convert_units  # imports conversion logic


class UnitConverterApp:  # defines the application window

    def __init__(self, root):
        self.root = root  # stores the main window
        self.root.title("Unit Converter")  # sets the window title
        self.root.geometry("440x400")  # sets the window size
        self.root.resizable(False, False)  # prevents resizing

        self.input_value = tk.StringVar()  # stores number input
        self.from_unit = tk.StringVar(value="Meters (m)")  # sets starting unit
        self.to_unit = tk.StringVar(value="Kilometers (km)")  # sets target unit
        self.output_value = tk.StringVar()  # stores conversion result

        self.create_widgets()  # builds the interface

    def create_widgets(self):  # creates interface elements
        main_frame = ttk.Frame(self.root, padding=20)  # creates main container
        main_frame.pack(fill="both", expand=True)  # fills the window

        ttk.Label(
            main_frame, text="Unit Converter", font=("Arial", 18, "bold")
        ).pack(pady=(0, 18))  # displays the heading

        ttk.Label(main_frame, text="Enter a number:").pack(anchor="w")  # labels input

        input_box = ttk.Entry(
            main_frame,
            textvariable=self.input_value,
            font=("Arial", 16),  # increases text size
            width=25  # sets input width
        )  # creates number input
        input_box.pack(fill="x", ipady=8, pady=(4, 12))  # increases box height
        input_box.focus()  # focuses the input box

        ttk.Label(main_frame, text="Convert from:").pack(anchor="w")  # labels source

        self.from_dropdown = ttk.Combobox(
            main_frame,
            textvariable=self.from_unit,
            values=list(UNITS.keys()),
            state="readonly",
        )  # creates starting-unit dropdown
        self.from_dropdown.pack(fill="x", pady=(4, 12))  # places dropdown

        ttk.Label(main_frame, text="Convert to:").pack(anchor="w")  # labels target

        self.to_dropdown = ttk.Combobox(
            main_frame,
            textvariable=self.to_unit,
            values=list(UNITS.keys()),
            state="readonly",
        )  # creates target-unit dropdown
        self.to_dropdown.pack(fill="x", pady=(4, 12))  # places dropdown

        convert_button = ttk.Button(
            main_frame, text="Convert", command=self.perform_conversion
        )  # creates conversion button
        convert_button.pack(fill="x", pady=(4, 12))  # places button

        ttk.Label(main_frame, text="Result:").pack(anchor="w")  # labels output

        output_box = ttk.Entry(
            main_frame,
            textvariable=self.output_value,
            state="readonly",
            font=("Arial", 16),  # increases result text size
            width=25  # sets output width
        )  # creates read-only output box
        output_box.pack(fill="x", ipady=8, pady=(4, 0))  # increases box height

        self.root.bind("<Return>", self.perform_conversion)  # converts on Enter

    def perform_conversion(self, event=None):  # handles conversion requests
        try: 
            number = float(self.input_value.get())  # converts input text to a number

            result = convert_units(
                number, self.from_unit.get(), self.to_unit.get()
            )  # performs conversion

            self.output_value.set(f"{result:.10g}")  # displays formatted result

            
        except ValueError as error: 
            self.output_value.set(f"Error: {error}")  # displays error message
