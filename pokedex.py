import csv
from prettytable import PrettyTable 

pokedex = PrettyTable()

with open(r"pokemon_datas/pokemon.csv", newline="") as rd:
    file = csv.reader(rd)
    pokedex.field_names = ["#", "Nombre", "Tipo 1", "Tipo 2", "Total", "HP",\
                       "Ataque", "Defensa","Ataque Especial", "Defensa Especial",\
                        "Velocidad", "Generación", "Legendario"]
    for fila in file:
        pokedex.add_row(fila)

while True:
    print("1. Busqueda por ID")
    #print("2. Busqueda por nombre:")
    print("3. Filtrar números de IDs de inicio a fin")
    print("4. Mostras Pokedex completa")
    print("5. Finalizar")

    option = int(input())

    match option:
        case 1: 
            id = int(input("ID: "))
            print(pokedex.get_string(start=id-1, end=id))
        
        #case 2:
            #nombre_buscar = input("Nombre del Pokemón: ")
            #for name in pokedex:
                #if name[0] == 2:

        case 3:
            id_1 = int(input("ID de inicio: "))
            id_2 = int(input("ID de fin: "))
            print(pokedex.get_string(start=id_1-1, end=id_2))
        
        case 4:
            print(pokedex)

        case 5:
            break