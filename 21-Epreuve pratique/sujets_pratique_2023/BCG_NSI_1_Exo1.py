# Créé par iako.pain, le 08/12/2023 en Python 3.7
def verifie(tableau):
    ord=tableau[0]
    for i in range(len(tableau)):
        if ord <= tableau[i]:
            ord = tableau[i]
        else:
            return False
    return True


print (verifie([5]))