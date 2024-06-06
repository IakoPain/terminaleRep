def indices_maxi(tab):
    list=[]
    max=tab[0]
    for m in range(len(tab)):
        if max<tab[m]:
            max=tab[m]
    for n in range(len(tab)):
        if max == tab[n]:
            list.append(n)
    return (max, list)