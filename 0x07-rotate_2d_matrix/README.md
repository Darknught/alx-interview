# Rotate 2D Matrix

## Description

This project involves writing a Python function to rotate a 2D matrix by 90 degrees clockwise. The function should modify the matrix in place without using any additional matrices.

## Process Explanation

To rotate a 2D matrix by 90 degrees clockwise, follow these two main steps:

1. **Transpose the Matrix**:
    - Transposing a matrix involves swapping the elements at positions `(i, j)` with the elements at positions `(j, i)` for all `i` and `j`.
    - By doing this, you effectively convert rows into columns.

2. **Reverse Each Row**:
    - After transposing the matrix, each row needs to be reversed.
    - This reversal changes the order of elements in each row, achieving the 90-degree clockwise rotation.

### Detailed Steps

#### Step 1: Transposing the Matrix

- Iterate over the upper triangular part of the matrix (including the diagonal).
- Swap the elements at positions `(i, j)` with the elements at positions `(j, i)`.
- This operation converts rows into columns.

#### Step 2: Reversing Each Row

- After transposing the matrix, iterate over each row.
- Reverse the order of elements in each row.
- This step adjusts the transposed columns to align with the desired 90-degree clockwise rotation.

### Expected Output Format

When printing the rotated matrix, ensure that each row is printed on a new line to clearly display the rotated matrix.

## Usage Instructions

1. **Save the Script**: Write your Python script that implements the rotation logic and save it in a file, for example, `rotate_matrix.py`.
2. **Make the Script Executable**: Ensure the script has executable permissions by running `chmod +x rotate_matrix.py`.
3. **Run the Script**: Execute the script by running `./rotate_matrix.py` from your terminal.


## Contributing

If you find any issues or have suggestions for improvements, please open an issue or create a pull request. Contributions are welcome!

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
