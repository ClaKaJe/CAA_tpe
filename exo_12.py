import math

# Définition de la classe Point
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

# Fonction pour calculer la distance euclidienne entre deux points
def DistanceEuclidienne(p1, p2):
    return math.sqrt((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2)

# Fonction pour trouver la paire de points la plus proche
def PlusProchePaire(n, Tab):
    if n < 2:
        return None, None, float('inf')  # Impossible de trouver une paire avec moins de deux points

    min_distance = float('inf')
    closest_pair = None

    # Parcourir toutes les paires de points
    for i in range(n):
        for j in range(i + 1, n):  # Pour éviter de calculer deux fois la même paire
            distance = DistanceEuclidienne(Tab[i], Tab[j])
            if distance < min_distance:
                min_distance = distance
                closest_pair = (Tab[i], Tab[j])

    return closest_pair[0], closest_pair[1], min_distance

# Exemple d'utilisation
if __name__ == "__main__":
    # Exemple de points
    points = [
        Point(1, 2),
        Point(4, 5),
        Point(5, 1),
        Point(7, 8)
    ]
    n = len(points)
    
    point1, point2, distance = PlusProchePaire(n, points)
    
    print(f"Les deux points les plus proches sont : ({point1.x}, {point1.y}) et ({point2.x}, {point2.y})")
    print(f"La distance minimale est : {distance}")
