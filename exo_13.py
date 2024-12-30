def estPremier(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    for d in range(2, int(n**0.5) + 1):
        if n % d == 0:
            return False
    return True

def listePremiers(n):
    return [i for i in range(2, n + 1) if estPremier(i)]

def valuation_p_adique(n, p):
    if n <= 0 or p <= 1 or not estPremier(p):
        return 0
    count = 0
    while n % p == 0:
        n //= p
        count += 1
    return count

def decomposition_facteurs_premiers(n):
    facteurs = []
    valuations = []
    for p in listePremiers(n):
        v = valuation_p_adique(n, p)
        if v > 0:
            facteurs.append(p)
            valuations.append(v)
    return [facteurs, valuations]

def AfficheDecomposition(Tab):
    return [(Tab[0][i], Tab[1][i]) for i in range(len(Tab[0]))]

# Test complet
n = 29689704
Tab = decomposition_facteurs_premiers(n)
print(f"Décomposition de {n} : {AfficheDecomposition(Tab)}")
