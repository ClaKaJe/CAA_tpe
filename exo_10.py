# Fonction extrait
def extrait(nb):
    if nb < 10:
        return -1, nb
    premier_chiffre = int(str(nb)[0])  # Prend le premier chiffre
    nb = int(str(nb)[1:])  # Retire le premier chiffre
    return premier_chiffre, nb

# Fonction palindrome
def palindrome(nb):
    original = str(nb)
    inverse = original[::-1]
    return original == inverse

# Programme principal
while True:
    try:
        nb = int(input("Entrez un nombre entier (ou -1 pour quitter) : "))
        if nb == -1:
            break
        if palindrome(nb):
            print(f"{nb} est un palindrome.")
        else:
            print(f"{nb} n'est pas un palindrome.")
    except ValueError:
        print("Veuillez entrer un entier valide.")
