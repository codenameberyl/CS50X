def main():
    card_number = input("Number: ")

    if is_valid(card_number):
        if is_amex(card_number):
            print("AMEX")
        elif is_mastercard(card_number):
            print("MASTERCARD")
        elif is_visa(card_number):
            print("VISA")
        else:
            print("INVALID")
    else:
        print("INVALID")


# Check if the card number is valid using Luhn's algorithm
def is_valid(card_number):
    card_number = card_number[::-1]  # Reverse the card number
    total = 0

    for i in range(len(card_number)):
        digit = int(card_number[i])
        if i % 2 == 1:
            digit *= 2
            if digit > 9:
                digit -= 9
        total += digit

    return total % 10 == 0


# Check if the card number is an American Express card
def is_amex(card_number):
    return len(card_number) == 15 and (
        card_number[:2] == "34" or card_number[:2] == "37"
    )


# Check if the card number is a MasterCard
def is_mastercard(card_number):
    return len(card_number) == 16 and 51 <= int(card_number[:2]) <= 55


# Check if the card number is a Visa card
def is_visa(card_number):
    return (len(card_number) == 13 or len(card_number) == 16) and card_number[0] == "4"


if __name__ == "__main__":
    main()
