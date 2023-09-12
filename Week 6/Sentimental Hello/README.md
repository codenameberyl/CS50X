# Sentimental / Hello

This Python program is an implementation to [CS50’s Introduction to Computer Science Week 6 - Sentimental / Hello Problem Set](https://cs50.harvard.edu/x/2023/psets/6/hello/). This simple Python program prompts the user for their name and then prints out a personalized greeting. The program is designed to introduce you to basic user input and output in Python.

## Getting Started

1. Make sure you have Python installed on your machine.
2. Download the program files by running the following commands in your terminal:

    ```bash
    cd "Sentimental / Hello"
    ```

3. Run the program by executing the command `python hello.py`.

## Program Structure

- `hello.py`: The main Python program that prompts the user for their name and prints a greeting.

## Usage

1. Open a terminal and navigate to the `"Sentimental / Hello"` directory.
2. Run the program using the command `python hello.py`.

## How the Program Works

1. The program starts by defining a function called `main`. This function is the entry point of the program.
2. Inside the `main` function, the program uses the `input` function to prompt the user for their name.
3. The user's input is stored in the variable `name`.
4. The program then uses the `print` function to display the greeting, which includes the user's name.

## Testing

You can test the program by running it and providing different names as input. For example:

```bash
$ python hello.py
What's your name?
Alice
hello, Alice
```

## Additional Notes

- The program uses the `input` function to get user input. The `input` function displays a prompt to the user and waits for them to enter a value, which is then returned as a string.
- The `print` function is used to display output to the user. In this case, it prints the greeting along with the user's name.
- The program follows the best practice of encapsulating the main code within a `main` function and then checking if the script is being run as the main program using the `__name__` variable.
- Feel free to experiment with the program by customizing the prompt and the greeting message.

Remember that this program is a simple example to demonstrate basic input and output in Python. It's a starting point to learn about these fundamental concepts in programming.