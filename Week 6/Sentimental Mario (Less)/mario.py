def main():
    while True:
        try:
            n = int(input("Height: "))
            if n > 0 and n < 9:
                for i in range(n):
                    print(" " * (n - i - 1) + "#" * (i + 1))
                break
        except ValueError:
            continue


if __name__ == "__main__":
    main()