# -*- coding: utf-8 -*-
"""
Created on Fri Sep 27 11:42:30 2024

@author: HP EliteBook 840 G4
"""

import tkinter as tk
from tkinter import Scrollbar

# Define the Application class
class MyApp:
    def __init__(self, root):
        # Set the window title
        self.root = root
        self.root.title("GUI with OOP, Scrollbar, and Multiple Buttons")
        
        # Create and place a label
        self.label = tk.Label(self.root, text="Welcome to the App!", font=("Arial", 16))
        self.label.pack(pady=10)
        
        # Create a Text widget (which will be scrollable)
        self.text_box = tk.Text(self.root, height=40, width=40, wrap="word")
        self.text_box.pack(side=tk.LEFT, padx=40, pady=40)

        # Add some example text to the Text widget
        self.text_box.insert(tk.END, "This is a scrollable text area.\n" * 10)
        
        # Create and place a scrollbar
        self.scrollbar = Scrollbar(self.root, command=self.text_box.yview)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        # Connect the Text widget and Scrollbar
        self.text_box.config(yscrollcommand=self.scrollbar.set)

        # Create a button to change the label text
        self.button_change_text = tk.Button(self.root, text="Change Label", command=self.on_change_label_click)
        self.button_change_text.pack(pady=5)

        # Create a button to clear the text area
        self.button_clear_text = tk.Button(self.root, text="Clear Text Area", command=self.on_clear_text_click)
        self.button_clear_text.pack(pady=5)

        # Create a button to append more text
        self.button_append_text = tk.Button(self.root, text="Append Text", command=self.on_append_text_click)
        self.button_append_text.pack(pady=5)

    # Function to change the label when the button is clicked
    def on_change_label_click(self):
        self.label.config(text="Label Changed!")

    # Function to clear the text area
    def on_clear_text_click(self):
        self.text_box.delete(1.0, tk.END)  # Clear all text

    # Function to append more text to the text area
    def on_append_text_click(self):
        self.text_box.insert(tk.END, "\nAppended text here!")

# Main program execution
if __name__ == "__main__":
    # Create the main window (root)
    root = tk.Tk()

    # Create an instance of MyApp with root window
    app = MyApp(root)

    # Run the application
    root.mainloop()
