from sys import argv
import sys
#from ctype import isalpha, isupper, islower

def main():
    k = prompt()
    plaintext = input("plaintext: ")
    switch(k, plaintext)

def prompt():
    if len(sys.argv) != 2:
        print("you have to type more")
        exit(1)
    elif len(argv) == 2:
        if not int(sys.argv[1]):
            print("it must be a number")
            exit(1)
        elif int(sys.argv[1]):
            k = int(sys.argv[1])

    return k



def switch(k, plaintext):
    print("ciphertext: ", end = "")
    for i in plaintext:
        if i.isalpha():
            if i.islower():
                p = ord(i) - ord("a")
                c = (p + k) % 26
                char = chr(c + ord("a"))
            elif i.isupper():
                p = ord(i) - ord("A")
                c = (p + k) % 26
                char = chr(c + ord("A"))
        else:
            char = i

        print(char, end = "")

    print()

if __name__ == "__main__":
    main()

