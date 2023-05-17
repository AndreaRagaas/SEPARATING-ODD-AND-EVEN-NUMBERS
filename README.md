# Odd and Even Numbers Program

This Python program reads a text file named `numbers.txt` that contains 20 integers. The program creates two other text files: `even.txt`, which contains all the even numbers extracted from `numbers.txt`, and `odd.txt`, which contains all the odd numbers extracted from `numbers.txt`.

## Program Flow

1. The program starts by opening the `numbers.txt` file in read mode using the `open()` function.

2. Two lists, `even_numbers` and `odd_numbers`, are created by extracting even and odd numbers, respectively, from the lines read from `numbers.txt`.

3. The odd numbers are written to the `odd.txt` file, and the even numbers are written to the `even.txt` file using the `write()` method within a `with` statement. Each number is written on a separate line.

4. The program then displays a header and options for the user in the console.

5. A `MENU()` function is defined to handle user input and display the corresponding numbers based on the selected option.

6. Within the `MENU()` function, the user is prompted to enter a choice.

7. If the choice is 1, the program reads and prints the contents of the `odd.txt` file.

8. If the choice is 2, the program reads and prints the contents of the `even.txt` file.

9. If the choice is 3, the program exits with a goodbye message.

10. If the choice is invalid (not 1, 2, or 3), an error message is displayed, and the user is prompted again.

11. Finally, the program closes the `numbers.txt` file.

## Usage

1. Create a text file named `numbers.txt` and populate it with 20 integers, each on a separate line.

2. Save the code in a Python file with a `.py` extension, e.g., `odd_even_numbers.py`.

3. Run the Python script.

4. The program will create two text files, `odd.txt` and `even.txt`, in the same directory as the Python script. These files will contain the odd and even numbers extracted from `numbers.txt`, respectively.

5. The program will display a header and a menu with options in the console.

6. Enter the corresponding number for the option you want to select:

   - Entering `1` will display the odd numbers extracted from `numbers.txt`.
   - Entering `2` will display the even numbers extracted from `numbers.txt`.
   - Entering `3` will exit the program.

7. Follow the prompts and view the displayed numbers based on your chosen option.

8. Once you select the exit option (`3`), the program will terminate.

**Note:** Make sure to provide valid integer inputs in the `numbers.txt` file for the program to work correctly.
