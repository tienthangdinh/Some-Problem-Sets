from cs50 import get_float

while True:
    geld = get_float("Change owed: ")
    if geld > 0:
        break

money = round(geld * 100)
a = 0
b = 0
c = 0
d = 0

while money > 25 or money == 25:
    money = money - 25
    a = a + 1

while money > 10 or money == 10:
    money = money - 10
    b = b + 1

while money > 5 or money == 5:
    money = money - 5
    c = c + 1
d = money % 5

print(f"{a+b+c+d}")

