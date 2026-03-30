# INHERITANCE-POLYMORPHISM

# 1. Fibonacci Series Generator

A Python application that generates the Fibonacci series using both iterative and recursive methods. The application has a graphical user interface (GUI) built with Tkinter, allowing users to input the number of terms they want to generate, and it provides two options for series generation: Iterative and Recursive.

## Features

- **Iterative Fibonacci**: Uses an iterative approach to generate the Fibonacci series.
- **Recursive Fibonacci**: Uses recursion to generate the Fibonacci series.
- **GUI**: Provides a simple Tkinter-based GUI where users can input the number of terms and choose the method to generate the series.
- **Error Handling**: Handles invalid input, ensuring users can only enter positive integers.

## Requirements

- Python 3.x
- Tkinter (typically comes pre-installed with Python)

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/NehalSolanki01/Inheritance-Polymorphism.git
   ```

2. Navigate to the project folder:

   ```bash
   cd Inheritance-Polymorphism
   ```

3. Run the Python script:

   ```bash
   python fibonacci_gui.py
   ```

   (Note: If your system does not have Tkinter installed, you may need to install it separately. On most systems, Tkinter comes pre-installed with Python.)

## Code Explanation

### 1. `SeriesGenerator` (Base Class)
The `SeriesGenerator` class is an abstract base class that defines the method `generate_series(n)`. This method should be overridden in the subclasses to implement specific series generation logic.

### 2. `FibonacciIterative` (Iterative Method)
The `FibonacciIterative` class inherits from `SeriesGenerator` and implements the `generate_series(n)` method iteratively. It starts with `a=0` and `b=1`, and for each term, it appends `a` to the series and updates `a` and `b` accordingly.

### 3. `Fib_Recursive` (Recursive Method)
The `Fib_Recursive` class also inherits from `SeriesGenerator` and implements the `generate_series(n)` method recursively. A helper function `fib(num)` is used to calculate the nth Fibonacci number by recursively calling itself.

### 4. `Fib_GUI` (Graphical User Interface)
The `Fib_GUI` class creates a Tkinter window that allows the user to:
- Enter the number of terms to generate.
- Choose between the iterative or recursive method to generate the Fibonacci series.
- Display the generated Fibonacci series.

The `generate_series` method takes a `generator` instance as an argument (either `FibonacciIterative` or `Fib_Recursive`) and generates the series based on user input. It also handles invalid input by displaying an error message.

### 5. Running the Application
When the script is run, the `Fib_GUI` class initializes a Tkinter window where users can input the number of terms they wish to generate, and click the respective buttons to generate the Fibonacci series either iteratively or recursively.

### Example Usage
1. **Enter the number of terms** (e.g., 10).
2. **Click "Generate Iteratively"** or **"Generate Recursively"**.
3. The Fibonacci series will be displayed on the window.

## Screenshots

![fib](https://github.com/user-attachments/assets/879f65f2-c9c6-46ed-b9cd-0069dc126c7d)



_____________________________________________________________________________________________________________________________________________________________________________________________________________________

# 2. GUI Application with OOP, Scrollbar, and Multiple Buttons

This project demonstrates a simple GUI application built with Python's `tkinter` library, utilizing object-oriented programming (OOP) principles. The application features a scrollable text area, a label, and multiple buttons that perform various actions.

## Features

- **Scrollable Text Area**: A `Text` widget that allows for scrolling through content, with an attached vertical scrollbar.
- **Label**: A label that displays a welcome message, which can be changed using a button.
- **Buttons**: 
  - **Change Label**: Updates the label text.
  - **Clear Text Area**: Clears all content in the text area.
  - **Append Text**: Adds more text to the text area.

## Code Structure

- **MyApp Class**: This class defines the GUI and its interactive elements.
  - `__init__(self, root)`: Initializes the main GUI components.
  - `on_change_label_click(self)`: Updates the label with a new message when the "Change Label" button is clicked.
  - `on_clear_text_click(self)`: Clears the text area.
  - `on_append_text_click(self)`: Appends additional text to the text area.

## Getting Started

### Prerequisites

- Python 3.x: Ensure that Python is installed on your system. [Download Python](https://www.python.org/downloads/)

### Installation

1. Clone this repository or download the `GUI_OOP_Scrollbar.py` file.
2. Navigate to the directory containing the file.

### Running the Application

To run the application, use the following command in the terminal:

```bash
python GUI_OOP_Scrollbar.py
```

This will open the application window, displaying the label, text area, and buttons.

## Usage

- **Change Label**: Click this button to change the label text to "Label Changed!"
- **Clear Text Area**: Click this button to clear all text in the scrollable text area.
- **Append Text**: Click this button to add more text at the end of the text area.

## Example Screenshot

![GUI_Scrollbar](https://github.com/user-attachments/assets/36b9a61c-baf2-4407-9fb4-fc53a2659cc6)


____________________________________________________________________________________________________________________________________________________________________________________________________________________

# 3. Grade Percentage Calculator

This is a simple Python GUI application built with `tkinter` to calculate the percentage of marks based on the grade level. The application demonstrates the concept of polymorphism in object-oriented programming by defining different grade levels with varying numbers of subjects.

## Features

- **Grade Selection**: Allows users to select between Grade 1, Grade 2, and Grade 3.
- **Subject Mark Entries**: Dynamically adjusts the number of subject entry fields based on the selected grade.
  - Grade 1: 3 subjects
  - Grade 2: 4 subjects
  - Grade 3: 5 subjects
- **Percentage Calculation**: Calculates and displays the percentage based on the entered marks for the selected grade.

## Code Structure

The main components of the code include:

- **Grade Classes**:
  - `Grade`: A base class with an abstract `calculate_percentage` method.
  - `Grade1`, `Grade2`, `Grade3`: Subclasses that calculate the percentage based on the number of subjects for each grade level.

- **Functions**:
  - `update_subject_entries`: Updates the number of visible entry fields based on the selected grade.
  - `calculate_percentage`: Gathers marks from the visible entries, calculates the percentage using the selected grade's calculation method, and displays the result.

## Getting Started

### Prerequisites

- **Python 3.x**: Ensure Python is installed. [Download Python](https://www.python.org/downloads/)

### Running the Application

1. Save the code in a file named `grade_percentage_calculator.py`.
2. Run the application with:

    ```bash
    python grade_percentage_calculator.py
    ```

This will open a window for the Grade Percentage Calculator.

## Usage

1. **Select Grade**: Choose a grade level from the dropdown menu.
2. **Enter Marks**: Input the marks for each subject displayed.
3. **Calculate Percentage**: Click "Calculate Percentage" to see the result. A message box will display the calculated percentage.

## Example Screenshot

![Grade](https://github.com/user-attachments/assets/a7141b9b-7705-4ddb-b70c-4fcdf3fa7718)


## Contributing

Feel free to fork the repository and submit pull requests. If you encounter any issues or have suggestions for improvements, please open an issue.

## License

This project is open-source and available under the MIT License.



