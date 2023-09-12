def main():
    while True:  # Creating a loop for the value of n after the user's input
        try:
            n = int(input("Height: "))  # Prompting the user for a positive integer
            if n > 0 and n < 9:
                for i in range(n):
                    print(" " * (n - i - 1) + "#" * (i + 1) + "  " + "#" * (i + 1))
                break
        except ValueError:
            continue


if __name__ == "__main__":
    main()