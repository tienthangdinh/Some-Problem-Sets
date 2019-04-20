from cs50 import get_int

while True:
    number = get_int("Number: ")
    if number > 0:
        break

stringnumber = str(number)
summe1 = 0
summe2 = 0

if len(stringnumber) % 2 == 0:
    for i in range(0, len(stringnumber) - 1, 2):
        a = int(stringnumber[i]) * 2
        for j in range(len(str(a))):
            summe1 = summe1 + int(str(a)[j])
    for i in range(1, len(stringnumber), 2):
        summe2 = summe2 + (int(stringnumber[i]))
    summe = summe1 + summe2

if len(stringnumber) % 2 == 1:
    for i in range(1, len(stringnumber), 2):
        a = int(stringnumber[i]) * 2
        for j in range(len(str(a))):
            summe1 = summe1 + int(str(a)[j])
    for i in range(0, len(stringnumber) - 1, 2):
        summe2 = summe2 + (int(stringnumber[i]))
    summe = summe1 + summe2

if summe % 10 != 0:
    print("INVALID")
elif summe % 10 == 0:
    if len(stringnumber) == 15 and stringnumber[0] == "3":
        if stringnumber[1] =="4" or stringnumber[1] == "7":
            print("AMEX")
    elif len(stringnumber) == 16 and stringnumber[0] == "5":
        if stringnumber[1] =="1" or stringnumber[1] == "2" or stringnumber[1] == "3" or stringnumber[1] == "4" or stringnumber[1] == "5":
            print("MASTERCARD")
    elif len(stringnumber) == 16 or len(stringnumber) == 13:
        if stringnumber[0] == "4":
            print("VISA")






