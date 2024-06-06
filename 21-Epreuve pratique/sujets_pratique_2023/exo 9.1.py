def multipli(n1,n2):
    if n1<0:
        return -multipli(-n1,n2)
    if n2<0:
        return -multipli(n1,-n2)
    resultat = 0
    for n in range(n2):
        resultat+=n1
    return resultat

print (multipli(3,5))
print (multipli(-4,-8))
print (multipli(-2,6))
print (multipli(-2,0))