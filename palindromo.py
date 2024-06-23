def palindromo(text:str):
    reversed_text = "".join([text[-i] for i in range(1, len(text) + 1)])
    if reversed_text != text:
        print("\nNo es palindromo")
    else:
        print("\nSí es")

word = input("Escribe para verificar si es palindromo o no: ")
palindromo(word)