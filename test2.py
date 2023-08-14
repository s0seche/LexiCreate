chaine = "baptiste1911!"
caractere_a_remplacer = "ai"
nouveau_caractere = "@$"

chaine_modifiee = chaine

for ancien, nouveau in zip(caractere_a_remplacer, nouveau_caractere):
    chaine_modifiee = chaine_modifiee.replace(ancien, nouveau)

    print(chaine_modifiee)
print(chaine_modifiee)
