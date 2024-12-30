from datetime import date

# Fonction pour vérifier si une année est bissextile
def Bissextile(annee):
    if (annee % 4 == 0 and annee % 100 != 0) or (annee % 400 == 0):
        return 1  # Année bissextile
    return 0  # Année non bissextile

# Fonction pour obtenir le nombre de jours dans un mois donné d'une année
def NbrJoursMois(mois, annee):
    if mois in [1, 3, 5, 7, 8, 10, 12]:  # Mois à 31 jours
        return 31
    elif mois in [4, 6, 9, 11]:  # Mois à 30 jours
        return 30
    elif mois == 2:  # Février
        return 29 if Bissextile(annee) else 28
    else:
        raise ValueError("Le mois doit être compris entre 1 et 12.")

# Fonction pour valider une date
def ValideDate(jour, mois, annee):
    try:
        date(annee, mois, jour)
        return 1  # Date valide
    except ValueError:
        return 0  # Date invalide

# Fonction pour calculer le nombre de jours vécus depuis la naissance
def NbrJours(date_naissance, date_actuelle):
    # Convertir les dates en objets `date`
    dn = date(date_naissance['Annee'], date_naissance['Mois'], date_naissance['Jour'])
    da = date(date_actuelle['Annee'], date_actuelle['Mois'], date_actuelle['Jour'])
    
    # Calculer la différence en jours
    difference = (da - dn).days
    return difference

# Exemple d'utilisation
if __name__ == "__main__":
    # Date de naissance (exemple)
    date_naissance = {"Jour": 18, "Mois": 1, "Annee": 1965}

    # Date actuelle (peut être remplacée par une date spécifique)
    date_actuelle = {"Jour": 30, "Mois": 12, "Annee": 2024}

    # Vérification des dates
    if ValideDate(date_naissance["Jour"], date_naissance["Mois"], date_naissance["Annee"]) and \
       ValideDate(date_actuelle["Jour"], date_actuelle["Mois"], date_actuelle["Annee"]):
        
        # Calcul du nombre de jours
        jours_vécus = NbrJours(date_naissance, date_actuelle)
        print(f"Nombre de jours vécus : {jours_vécus}")
    else:
        print("Une ou les deux dates fournies sont invalides.")
