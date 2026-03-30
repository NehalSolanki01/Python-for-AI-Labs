# OOP -Object-oriented Programming

# 1. Movie Rating System

This Python program rates movies based on four parameters: story, actors, music, and cinematography. Using object-oriented programming (OOP), the `MovieRating` class calculates an overall rating and provides a verdict on the movie's quality (Excellent, Good, Average, or Poor) based on the calculated score.

## Features

- **Rating Parameters**: Each movie is rated on a scale from 0 to 10 for the following parameters:
  - **Story**
  - **Actors**
  - **Music**
  - **Cinematography**
- **Overall Rating Calculation**: An average score is calculated from the four parameters.
- **Verdict**: The program provides a verdict on the movie's quality based on the overall rating:
  - 8 or higher: **Excellent**
  - 6 to 7.9: **Good**
  - 4 to 5.9: **Average**
  - Below 4: **Poor**

## Code Overview

- **MovieRating Class**: 
  - `__init__`: Initializes the movie attributes, ensuring each rating is between 0 and 10.
  - `verdict`: Returns a verdict based on the overall rating.
- **Object Instantiation**: Four movie objects (`movie1`, `movie2`, `movie3`, `movie4`) are created with different ratings, and their verdicts and overall ratings are printed.

## Usage

1. **Create a MovieRating Object**: Instantiate a `MovieRating` object by providing the movie name and ratings for story, actors, music, and cinematography.
2. **Get Verdict**: Call the `verdict` method to obtain the movie's quality assessment.
3. **Check Overall Rating**: Access the `overall_rating` attribute to view the average rating.

### Example

```python
# Creating a MovieRating object
movie1 = MovieRating("Interstellar", 9, 10, 10, 9)

# Get the verdict
print(movie1.verdict())  # Output: Interstellar is Excellent

# Check the overall rating
print(movie1.overall_rating)  # Output: 9.5
```

____________________________________________________________________________________________________________________________________________________________________________________________________________________


# 2. Library and Book Management System

This Python program provides a library management system, allowing users to add, remove, borrow, and return books. The system consists of two main classes: `Books` and `Library`. It demonstrates object-oriented programming concepts like encapsulation and class interaction.

## Features

- **Book Class** (`Books`): Represents a book with attributes such as title, author, page count, and year published.
- **Library Class** (`Library`): Manages a collection of books and supports various actions:
  - **Add Book**: Adds a book to the library.
  - **Remove Book**: Removes a book from the library.
  - **Borrow Book**: Allows a user to borrow a book if it’s available.
  - **Return Book**: Returns a borrowed book to the library.
  - **List Available Books**: Displays a list of books currently available in the library.

## Code Structure

- **Books Class**:
  - `__init__`: Initializes the book’s attributes.
  
- **Library Class**:
  - `__init__`: Initializes the library’s name and list of books.
  - `add_book`: Adds a book to the library.
  - `remove_book`: Removes a book from the library.
  - `borrow_book`: Marks a book as borrowed if it’s available.
  - `return_book`: Marks a borrowed book as returned.
  - `list_available_books`: Lists all books currently available in the library.

## Usage

1. **Create Book Objects**: Instantiate `Books` objects with title, author, page count, and year published.
2. **Add Books to Library**: Use `add_book` method to add books to the library.
3. **Borrow/Return Books**: Use `borrow_book` and `return_book` methods to manage book borrowing.
4. **List Available Books**: Use `list_available_books` to display all books currently available.

### Example

```python
# Create book objects
book1 = Books("The Great Gatsby", "F. Scott Fitzgerald", 180, 1925)
book2 = Books("1984", "George Orwell", 328, 1949)

# Create library
my_library = Library("Bibliotheek Loosduinen")

# Add books to library
my_library.add_book(book1)
my_library.add_book(book2)

# List available books
my_library.list_available_books()

# Borrow a book
print(my_library.borrow_book("1984"))

# List available books after borrowing
my_library.list_available_books()

# Return the borrowed book
print(my_library.return_book("1984"))

# List available books after returning
my_library.list_available_books()
```

## License

This project is open for personal and educational use.

