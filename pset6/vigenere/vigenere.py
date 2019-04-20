from sys import argv
import sys

def main():
    k = prompt()
    plaintext = input("plaintext: ")
    switch(k, plaintext)

def prompt():
    if len(sys.argv) != 2:
        print("bla bla bla")
        exit(1)
    elif len(sys.argv) == 2:
        for i in argv[1]:
            if not i.isalpha():
                print("must be alpha")
                exit(1)
        k = sys.argv[1]

    return k
    #remember that k is a word string

def switch(k, plaintext):
    print("ciphertext: ", end = "")
    index = 0
    secondstring = ""
    for i in range(len(plaintext)):
        if plaintext[i].isalpha():
            secondstring = secondstring + plaintext[i]

    thirdstring = ""
    for i in range(len(secondstring)):

        if secondstring[i].islower():
            p = ord(secondstring[i]) - ord("a")
            c = (p + ord(k[index].lower()) - ord("a")) % 26
            cha = chr(c + ord("a"))

        if secondstring[i].isupper():
            p = ord(secondstring[i]) - ord("A")
            c = (p +  ord(k[index].upper()) - ord("A")) % 26
            cha = chr(c + ord("A"))

        thirdstring = thirdstring + cha
        index = (index + 1) % len(k)

    counter = 0
    ciphertext = ""
    for i in range(len(plaintext)):
        if plaintext[i].isalpha():
            ciphertext = ciphertext + thirdstring[counter]
            counter = counter + 1
        if not plaintext[i].isalpha():
            ciphertext = ciphertext + plaintext[i]
    print(ciphertext)


if __name__ == "__main__":
    main()

