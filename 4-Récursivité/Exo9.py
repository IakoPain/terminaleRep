def recherche(lst,x):
    if len(lst)==0:
        return False
    m=len(lst) //2
    if lst[m]==x:
        return True
    elif x>lst[m]:
        return recherche(lst[:m],x)
    else:
        return recherche(lst[m+1:],x)
0,
lst=[2,5,9,12,15,21,34]

print(recherche(lst,4))
print(recherche(lst,12))
