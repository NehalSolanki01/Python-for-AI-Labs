# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 12:29:38 2024

@Nehal
"""

import tkinter as tk
from tkinter import messagebox

# Base class for series generation
class SeriesGenerator:
    def generate_series(self, n):
        raise NotImplementedError("This method should be overridden")

# Fibonacci generator using iterative method
class FibonacciIterative(SeriesGenerator):
    def generate_series(self, n):
        series = []
        a, b = 0, 1
        for i in range(n):
            series.append(a)
            a, b = b, a + b
        return series

# Fibonacci generator using recursive method
class Fib_Recursive(SeriesGenerator):
    def generate_series(self, n):
        def fib(num):
            if num <= 1:
                return num
            else:
                return fib(num - 1) + fib(num - 2)

        series = [fib(i) for i in range(n)]
        return series

# GUI Application
class Fib_GUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Fibonacci Series Generator")

        # Set window size to 400x400
        self.root.geometry("400x400")
        
        # Label
        self.label = tk.Label(root, text="Enter number of terms:")
        self.label.pack()
        
        # Entry for number of terms
        self.entry = tk.Entry(root)
        self.entry.pack()
        
        # Buttons
        self.iterative_button = tk.Button(root, text="Generate Iteratively", command=self.generate_iteratively)
        self.iterative_button.pack()

        self.recursive_button = tk.Button(root, text="Generate Recursively", command=self.generate_recursively)
        self.recursive_button.pack()
        
        # Display Area
        self.result_label = tk.Label(root, text="")
        self.result_label.pack()

    def generate_series(self, generator):
        try:
            n = int(self.entry.get())
            if n <= 0:
                raise ValueError("Enter a positive integer")
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid positive integer")
            return
        
        # Generate Fibonacci series
        series = generator.generate_series(n)
        self.result_label.config(text=f"Fibonacci Series: {series}")

    def generate_iteratively(self):
        self.generate_series(FibonacciIterative())

    def generate_recursively(self):
        self.generate_series(Fib_Recursive())

# Run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = Fib_GUI(root)
    root.mainloop()
   