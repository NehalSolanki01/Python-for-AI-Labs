# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 17:56:46 2024

@author: HP EliteBook 840 G4
"""

import tkinter as tk
from tkinter import messagebox

# Polymorphism with classes for different grades
class Grade:
    def calculate_percentage(self, marks):
        pass

class Grade1(Grade):
    def calculate_percentage(self, marks):
        total_marks = 300  # Assuming 3 subjects, 100 marks each
        return (sum(marks) / total_marks) * 100

class Grade2(Grade):
    def calculate_percentage(self, marks):
        total_marks = 400  # Assuming 4 subjects, 100 marks each
        return (sum(marks) / total_marks) * 100

class Grade3(Grade):
    def calculate_percentage(self, marks):
        total_marks = 500  # Assuming 5 subjects, 100 marks each
        return (sum(marks) / total_marks) * 100

# Function to update the number of entry fields based on selected grade
def update_subject_entries(*args):
    selected_grade = grade_var.get()
    
    # Clear existing entries
    for entry in entries:
        entry.grid_remove()

    # Show only the number of entries required for the selected grade
    if selected_grade == "Grade 1":
        num_subjects = 3
    elif selected_grade == "Grade 2":
        num_subjects = 4
    else:
        num_subjects = 5
    
    for i in range(num_subjects):
        entries[i].grid(row=2 + i, column=0, columnspan=2)

# Function to calculate the percentage based on grade and inputs
def calculate_percentage():
    selected_grade = grade_var.get()
    marks = []
    try:
        for entry in entries:
            if entry.winfo_ismapped():  # Only consider visible entries
                marks.append(int(entry.get()))
        if selected_grade == "Grade 1":
            grade = Grade1()
        elif selected_grade == "Grade 2":
            grade = Grade2()
        elif selected_grade == "Grade 3":
            grade = Grade3()
        percentage = grade.calculate_percentage(marks)
        messagebox.showinfo("Result", f"Your percentage is {percentage:.2f}%")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers for marks.")

# GUI setup
root = tk.Tk()
root.title("Grade Percentage Calculator")
root.geometry("400x400")  # Set the window size to 400x400

tk.Label(root, text="Select Grade:").grid(row=0, column=0)

grade_var = tk.StringVar(value="Grade 1")
grade_var.trace("w", update_subject_entries)  # Call when grade changes
grades = ["Grade 1", "Grade 2", "Grade 3"]
grade_menu = tk.OptionMenu(root, grade_var, *grades)
grade_menu.grid(row=0, column=1)

tk.Label(root, text="Enter Marks for Subjects:").grid(row=1, column=0, columnspan=2)

# Entries for subjects
entries = [tk.Entry(root) for _ in range(5)]
update_subject_entries()  # Initialize entries for default grade (Grade 1)

# Button to calculate percentage
calculate_button = tk.Button(root, text="Calculate Percentage", command=calculate_percentage)
calculate_button.grid(row=7, column=0, columnspan=2)

root.mainloop()
