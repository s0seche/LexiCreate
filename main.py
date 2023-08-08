#!/usr/bin/env python3

from itertools import product  

output = "output.txt"

alphabet ="abcdefghijqlmnopqrstuvwxyz"
uppercase =  alphabet.upper()
chelou = ["@","/","#",' ']
#chelou = "&~#{@+=€|ç/*-"
number_information = int(input("Indiquez le nombre d'informations que vous avez sur  votre cible "))
number =  "0123456789"
information = []
count = 0
for i in range(number_information):
	test = input("Indiquez l'information de la cible    ")
	test = test.lower()
	information.append(test)
	#information += test
	print (information)



with open(output, 'w') as f:
    for r in range(1, len(information) + 1):
        temp = product(information, repeat=r)
        for combination in list(temp):
            count += 1
            for element in combination:
                f.write(str(element) + ' ' )
            f.write('\n')  # Écrit une nouvelle ligne après chaque combinaison dans le fichier



print("Il existe" ,count, "possibilité")

#mettre des caracètes spéciaux dans la string et entre les 2 