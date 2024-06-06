def binaire(a):
    '''convertit un nombre entier a en sa representation
    binaire sous forme de chaine de caractères.'''
    if a == 0:
        return (0)
    bin_a = 0
    while a!=0 :
        bin_a = a + bin_a
        a = a*10
    return bin_a


