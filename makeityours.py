import time
import tkinter as tk
name = "Parkman"
opt_list = ["1", "2"]
print("Hi, I'm " + name + "!")
opt = input("Would you like to: 1. Help me figure out my age or 2. Select THE OTHER OPTION. Enter a 1 or 2 to make your selection: ")
while opt not in opt_list:
        opt = input("Please input a valid integer (1 or 2): ")
if opt in opt_list:
        opt = int(opt)
if opt == 1:
    age = input("How old am I?")
    print("I am " + age + " years old (at least according to you)")
elif opt == 2:
    print("You have selected THE OTHER OPTION")
    time.sleep(0.5)
    while True:
          root = tk.Tk()
          root.title("THE OTHER OPTION")
          root.geometry("700x300")
          root.attributes('-fullscreen', True)
          root.configure(bg = 'black')
          label = tk.TextLabel = tk.Label(root, text="YOU  CANNOT  ESCAPE  THE  OTHER  OPTION", font=("papyrus", 16, "bold"), fg = ("#ff0000"), bg = ("black"))
          label.pack(pady=120)
          root.mainloop()


