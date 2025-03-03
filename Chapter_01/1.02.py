"""
Code illustration: 1.02
Adding some widgets
Tkinter GUI Application Development Blueprints
"""

import tkinter as tk
root = tk.Tk()
my_label = tk.Label(root, text="I am a label widget")
my_button = tk.Button(root, text="I am a button")
my_label.pack()
my_button.pack()
root.mainloop()
