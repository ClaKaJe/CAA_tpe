def afficher_damier(n, p, C1, C2, methode):
    """Affiche un damier de taille n x n avec des cases de taille p x p en utilisant C1 et C2."""
    for i in range(n):
        for _ in range(p):  # Répéter p fois pour l'épaisseur de chaque ligne
            ligne = ""
            for j in range(n):
                if (i + j) % 2 == 0:
                    ligne += C1 * p  # Case noire
                else:
                    ligne += C2 * p  # Case blanche
            print(ligne)

def valider_entree():
    """Demande les entrées utilisateur et les valide."""
    while True:
        try:
            n = int(input("Entrez un nombre pair n (taille du damier) : "))
            p = int(input("Entrez un nombre entier p (taille des cases) : "))
            if n % 2 != 0 or not (1 <= n <= 9) or not (1 <= p <= 9):
                raise ValueError("n doit être pair et compris entre 1 et 9, p doit être compris entre 1 et 9.")
            C1 = input("Entrez un caractère C1 : ")
            C2 = input("Entrez un caractère C2 : ")
            if C1 == C2 or len(C1) != 1 or len(C2) != 1:
                raise ValueError("C1 et C2 doivent être différents et constitués d'un seul caractère.")
            return n, p, C1, C2
        except ValueError as e:
            print(f"Erreur : {e}. Veuillez réessayer.")

def menu_interactif():
    """Affiche le menu interactif pour choisir la méthode."""
    while True:
        print("\nMENU :")
        print("a) Afficher le damier avec une boucle FOR.")
        print("b) Afficher le damier avec une boucle WHILE.")
        print("c) Afficher le damier avec une boucle DO-WHILE simulée.")
        print("d) Changer les paramètres n, p, C1 et C2.")
        print("0) Quitter.")
        
        choix = input("Votre choix : ").lower()
        if choix == "0":
            print("Au revoir !")
            break
        elif choix in ["a", "b", "c", "d"]:
            n, p, C1, C2 = valider_entree()
            
            if choix == "a":
                print("Affichage du damier avec une boucle FOR :")
                afficher_damier(n, p, C1, C2, methode="for")
            elif choix == "b":
                print("Affichage du damier avec une boucle WHILE :")
                afficher_damier_while(n, p, C1, C2)
            elif choix == "c":
                print("Affichage du damier avec une boucle DO-WHILE (simulée) :")
                afficher_damier_do_while(n, p, C1, C2)
            elif choix == "d":
                print("Modification des paramètres.")
        else:
            print("Choix invalide. Veuillez réessayer.")

def afficher_damier_while(n, p, C1, C2):
    """Affiche le damier en utilisant une boucle WHILE."""
    i = 0
    while i < n:
        ligne_p = 0
        while ligne_p < p:
            j = 0
            ligne = ""
            while j < n:
                if (i + j) % 2 == 0:
                    ligne += C1 * p
                else:
                    ligne += C2 * p
                j += 1
            print(ligne)
            ligne_p += 1
        i += 1

def afficher_damier_do_while(n, p, C1, C2):
    """Affiche le damier en simulant une boucle DO-WHILE."""
    i = 0
    while True:
        ligne_p = 0
        while True:
            j = 0
            ligne = ""
            while True:
                if (i + j) % 2 == 0:
                    ligne += C1 * p
                else:
                    ligne += C2 * p
                j += 1
                if j >= n:
                    break
            print(ligne)
            ligne_p += 1
            if ligne_p >= p:
                break
        i += 1
        if i >= n:
            break

# Lancer le programme
if __name__ == "__main__":
    menu_interactif()
