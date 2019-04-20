from cs50 import get_string
from sys import argv


def main():
    if len(argv) != 2:
        print("python bleep.py dictionary")
        exit(1)
    else:
        dictionary = set()
        file = open(argv[1], "r")

        for line in file:
            dictionary.add(line.strip("\n")) #.strip in line works little bit anders als in string, it automatically strip the blank space at the end

        string = get_string("What message would you like to censor? \n")
        for i in string.split():
            if i.lower() not in dictionary:
                print(i, end = " ")
            elif i.lower() in dictionary:
                print("*" * len(i), end=" ")
        print()


if __name__ == "__main__":
    main()
