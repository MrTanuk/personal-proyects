"""Function to print like a hacker"""
from random import choice
from time import sleep
from string import ascii_letters

def random_text(randomize_text):
    """text hacker"""
    letters_randomized = ""
    size_text = len(randomize_text)
    for i in range(size_text + 1):
        for j in range(10):
            letters_randomized = "".join([choice(ascii_letters) for x in range(size_text)])
            letters_randomized = letters_randomized.replace(letters_randomized[:i], randomize_text[:i])
            print(letters_randomized)
            sleep(0.02)
            if i == size_text and j == 0:
                break

def main():
    """Main function"""
    text = input("Escribe el texto que quieres imprimir acá: ")
    random_text(text)

main()
