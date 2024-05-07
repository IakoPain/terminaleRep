def amis_d_amis(dico, pers):
    amis=(dico[pers])
    for i in range(len(amis)):
        amisamis+=(dico[ami[i]])
    return amisamis

dico = {'Ana': ['Bob'],'Bob': ['Ana', 'Erol'],'Erol': ['Bob', 'Filo', 'Dora','Gab'],'Filo': ['Gab'],'Carl': ['Bob'],'Dora': ['Gab'],'Gab': ['Erol']}
pers = 'Bob'
print(amis_d_amis)
