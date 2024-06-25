# UTF-8 Validation

This project provides a method to determine if a given data set represents a valid UTF-8 encoding. UTF-8 (Unicode Transformation Format - 8-bit) is a variable-width character encoding used for electronic communication, capable of encoding all possible characters in Unicode.

## Table of Contents
- [Overview](#overview)
- [Installation](#installation)
- [Usage](#usage)
- [Examples](#examples)
- [Testing](#testing)
- [Contributing](#contributing)
- [License](#license)

## Overview

UTF-8 is a widely used encoding system that supports a vast range of characters from different languages and symbol sets. This project includes a function `validUTF8` that checks if a list of integers represents a valid UTF-8 encoded data set. Each integer in the list represents a byte of data.

## Installation

No special installation is required for this project. Simply download the Python script and run it in your Python environment. Ensure you have Python 3.6 or higher installed.

## Usage

To use the `validUTF8` function, follow these steps:

1. Import the function into your script.
2. Pass a list of integers to the function.
3. The function returns `True` if the list represents a valid UTF-8 encoding, otherwise `False`.

```python
from utf8_validation import validUTF8

data = [197, 130, 1]
print(validUTF8(data))  # Output: True

data = [235, 140, 4]
print(validUTF8(data))  # Output: False
