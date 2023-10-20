def renduMonnaie(somme,pieces):
    choisies={}
    for p in pieces:
        choisies[p]=0
        while somme>=p:
            somme=somme-p
            choisies[p]+=1
    return choisies
pieces=[500,200,100,50,20,10,5,2,1]
somme=780
print('Les pièces choisies sont')
print(renduMonnaie(somme,pieces))