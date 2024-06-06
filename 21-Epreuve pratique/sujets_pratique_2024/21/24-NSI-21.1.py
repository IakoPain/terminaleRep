# Créé par iako.Pain, le 17/05/2024 en Python 3.7
def recherche_motif(motif,texte):
    liste = []
    total = 0
    for i in range(len(texte)):
        for j in range(len(motif)):
            if texte[i] == motif[j]:
                total +=1
                if total == len(motif):
                    liste.append(i)
    return liste

print (recherche_motif("ab", "abracadabraab"))


