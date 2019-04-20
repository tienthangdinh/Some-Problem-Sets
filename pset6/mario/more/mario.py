from cs50 import get_int

while True:
    a = get_int("Height: ")
    if a > 0 and a!=24:
        break
height = a

for i in range(height):
    for a in range(height - i - 1):
        print(" ", end = "")
    for b in range(i + 1):
        print("#", end = "")
    print("  ", end = "")
    for c in range(i + 1):
        print("#", end = "")
    print()


