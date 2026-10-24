import tkinter as tk  # imports Tkinter

from gui import UnitConverterApp  # imports the application interface


def main():  # starts the program
    root = tk.Tk()  # creates the main window
    UnitConverterApp(root)  # the converter interface
    root.mainloop()  # runs the gui event loop


if __name__ == "__main__":  # checks for direct execution
    main()  # launches the application
