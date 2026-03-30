# 3D_Array
# Random Password Generator

This Python script generates a random password by selecting characters from four different categories: uppercase letters, lowercase letters, digits, and special characters. It allows you to specify the length of the password and randomly picks characters from the available categories to create a secure password.

## Features

- **Customizable Password Length**: You can specify the length of the generated password.
- **Character Categories**: The password is composed of:
  - Uppercase letters (`A-Z`)
  - Lowercase letters (`a-z`)
  - Digits (`0-9`)
  - Special characters (`!@#$%^&*()_+-=[]{}|;':\",./<>?`)
- **Random Generation**: The password is generated randomly using the `random` module in Python.

## Requirements

- Python 3.x (or higher)
- No additional external libraries are required, only the built-in `random` module.

## How to Use

1. **Run the Script**:  
   You can run the script directly in your Python environment.

2. **Generate a Password**:  
   The function `generate_password(length)` generates a random password of the specified length.  
   - For example: `generate_password(12)` will generate a password of length 12.

3. **Output**:  
   The generated password will be displayed in the console.

## Code Explanation

- **Character Layers**: The script uses a 3D list (`array_3d`) containing four different layers:
  - Layer 1: Uppercase letters
  - Layer 2: Lowercase letters
  - Layer 3: Digits
  - Layer 4: Special characters
- **Random Selection**: The `generate_password` function randomly selects one character from any of the four layers for each position in the password.
- **Password Generation**: The function appends each randomly chosen character to the password list and then joins them to form a string.

## Example Code

```python
import random

# 3D array consisting of characters: uppercase, lowercase, digits, special characters
array_3d = [
    list("ABCDEFGHIJKLMNOPQRSTUVWXYZ"),  # Uppercase letters
    list("abcdefghijklmnopqrstuvwxyz"),  # Lowercase letters
    list("0123456789"),  # Digits
    list("!@#$%^&*()_+-=[]{}|;':\",./<>?")  # Special characters
]

# Function to generate password
def generate_password(length):
    password = []

    for i in range(length):
        layer = random.randint(0, 3)  # Randomly pick a layer from 0 to 3 (inclusive)

        if layer == 0:
            char = random.choice(array_3d[layer])  # Randomly pick a char from the uppercase letters
        elif layer == 1:
            char = random.choice(array_3d[layer])  # Randomly pick a char from the lowercase letters
        elif layer == 2:
            char = random.choice(array_3d[layer])  # Randomly pick a char from the digits
        elif layer == 3:
            char = random.choice(array_3d[layer])  # Randomly pick a char from the special characters

        password.append(char)

    return "".join(password)

# Example: Generate a password of length 10
password = generate_password(10)
print("Generated password:", password)
```

## Sample Output

```
Generated password: T^a2qg@9aJ
```

## Notes

- The password is generated randomly, so it will differ each time the script is run.
- You can adjust the password length by changing the argument passed to the `generate_password` function.
- The script uses the built-in `random` module to ensure that each character in the password is selected randomly from the available layers.

## License

This project is open-source and available under the MIT License.
