def main():
    while True:
        try:
            n = float(input("Change owed: "))
            if n > 0:
                break
        except ValueError:
            continue

    cents = round(n * 100)
    quarters = cents // 25  # Determine the number of quarters in cents
    dimes = (cents % 25) // 10  # Determine the number of dimes in cents
    nickels = ((cents % 25) % 10) // 5  # Determine the number of nickels in cents
    penny = (((cents % 25) % 10) % 5) // 1  # Determine the number of pennies in cents

    count = quarters + dimes + nickels + penny  # Calculating the remainder

    print(count)


if __name__ == "__main__":
    main()
