import sys

def main():
    cardnumber = get_number()
    checkcard(cardnumber)

def get_number():
    while True:
        cardnumber = input("Number: ")
        try:
            if len(cardnumber) > 0 and int(cardnumber):
                break
        except ValueError:
            continue

    return cardnumber

def checkcard(cardnumber):
    even, odd = 0, 0
    card_len = len(cardnumber)

    if card_len % 2 == 0:
        for i in range(card_len):
            if i % 2 == 0:
                a = int(cardnumber[i]) * 2
                if a >= 10:
                    a1 = a // 10
                    a2 = a % 10
                    even = even + a1 + a2
                else:
                    even = even + a
            elif i % 2 == 1:
                odd = odd + int(cardnumber[i])

    elif card_len % 2 == 1:
        for i in range(card_len):
            if i % 2 == 1:
                a = int(cardnumber[i]) * 2
                if a >= 10:
                    even = even + (a // 10)
                    even = even + (a % 10)
                else:
                    even = even + a
            elif i % 2 == 0:
                odd = odd + int(cardnumber[i])

    checksum = (even + odd) % 10

    if checksum != 0:
        print("INVALID")
        sys.exit(1)

    elif checksum == 0:
        first_digit = int(cardnumber[0])
        second_digit = int(cardnumber[1])
        if first_digit == 3 and second_digit == 4 or second_digit == 7:
            print("AMEX")
        elif first_digit == 5 and 1 <= second_digit <= 5:
            print("MASTERCARD")
        elif first_digit == 4:
            print("VISA")

if __name__ == "__main__":
    main()

