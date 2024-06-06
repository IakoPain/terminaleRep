def recherche(tab,n):
    indice = -1
    for p in range(len(tab)):
        if tab[p] == n:
            indice = p
    if indice == -1:
        return None
    else:
        return (indice)
