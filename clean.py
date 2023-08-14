#!/usr/bin/env python3

from itertools import product  

def generate_combinations(information, output_file):
    alphabet = "abcdefghijqlmnopqrstuvwxyz"
    uppercase = alphabet.upper()
    chelou = ["@", "/", "#", ' ']
    number = "0123456789"
    
    count = 0
    with open(output_file, 'w') as f:
        for r in range(1, len(information) + 1):
            temp = product(information, repeat=r)
            for combination in list(temp):
                count += 1
                for i, element in enumerate(combination):
                    f.write(str(element))
                    if i < len(combination) - 1:
                        f.write(chelou[i % len(chelou)])
                f.write('\n')  # Écrit une nouvelle ligne après chaque combinaison dans le fichier

    return count

def main():
    output = "output.txt"
    number_information = int(input("Indiquez le nombre d'informations que vous avez sur votre cible "))
    information = []
    
    for i in range(number_information):
        test = input("Indiquez l'information de la cible: ")
        test = test.lower()
        information.append(test)

    count = generate_combinations(information, output)

    print("Il existe", count, "possibilités")

if __name__ == "__main__":
    main()
