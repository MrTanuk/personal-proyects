import csv
from prettytable import PrettyTable 
import pandas as pd

pokedex = pd.read_csv("./pokemon_datas/pokemon.csv")

def main():
    while True:
        print("1. Mostras Pokedex completa")
        print("2. Busqueda por ID")
        print("3. Busqueda por nombre:")
        print("4. Filtrar números de IDs de inicio a fin")
        print("5. Finalizar")

        option = int(input("seleccione: "))
        match option:
            case 1:
                pd.set_option('display.max_rows', None)
                print(pokedex,"\n")
            case 2:
                id = int(input("Escriba la id: "))
                pokemon_by_id = pokedex.loc[pokedex['#'] == id]
                print(pokemon_by_id,"\n")
            case 3:
                name = input("Escriba el nombre: ")
                pokemon_by_name = pokedex.loc[pokedex['Name'] == name]
                print(pokemon_by_name,"\n")
            case 4:
                id_01 = int(input("Escriba el inicio: "))
                id_02 = int(input("Escriba el fin: "))
                pokemons_by_id =  pokedex.loc[pokedex['#'].between(id_01, id_02)]
                print(pokemons_by_id,"\n")
            case 5:
                break

if __name__ == "__main__":
    main()