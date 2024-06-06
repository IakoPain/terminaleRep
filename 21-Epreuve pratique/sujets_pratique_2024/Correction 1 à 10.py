# Créé par noe.brands, le 19/03/2024 en Python 3.7
# ex 1.1
a = {'F':['B','G'], 'B':['A','D'], 'A':['',''], 'D':['C','E'], 'C':['',''], 'E':['',''], 'G':['','I'], 'I':['','H'], 'H':['','']}


def taille(arbre, lettre):
    if lettre == '':
        return 0
    return 1 + taille(arbre, arbre[lettre][0]) + taille(arbre, arbre[lettre][1])

#ex 2.1
def correspond(mot, mot_a_trous):
    if len(mot) != len(mot_a_trous):
        return False
    for i in range(len(mot)):
        if mot[i] != mot_a_trous[i] and mot_a_trous[i] != '*':
            return False
    return True

#ex 3.1
def maximum_tableau(tab):
    maximum = tab[0]
    for element in tab:
        if element > maximum:
            maximum = element
    return maximum

#ex 4.1
def recherche(tab, n):
    indice_solution = None
    for i in range(len(tab)):
        if tab[i] == n:
            indice_solution = i
    return indice_solution

#ex 5.1
def max_et_indice(tab):
    val_max = tab[0]
    ind_max = 0
    for i in range(len(tab)):
        if tab[i] > val_max:
            val_max = tab[i]
            ind_max = i
    return (val_max, ind_max)

#ex 6.1
def verifie(tab):
    for i in range(1, len(tab)):
        if tab[i] < tab[i-1]:
            return False
    return True
#ex 7.1
def gb_vers_entier(tab):
    somme = 0
    for i in range(len(tab)):
        if tab[i]:
            somme += 2**(len(tab)-1-i)
    return somme

#ex 8.1
def delta(tab):
    diff = [tab[0]]
    for i in range(1, len(tab)):
        diff.append(tab[i] - tab[i-1])
    return diff

#ex9.1
def effectif_notes(notes_eval):
    tab = [0]*11
    for note in notes_eval:
        tab[note] += 1
    return tab

def notes_triees(eff):
    triees = []
    for i in range(11):
        if eff[i] != 0:
            for _ in range(eff[i]):
                triees.append(i)
    return triees

#ex10.1
def moyenne(tab):
    somme = 0
    coeffs = 0
    for couple in tab:
        somme += couple[0] * couple[1]
        coeffs += couple[1]
    if coeffs == 0:
        return None
    return somme / coeffs