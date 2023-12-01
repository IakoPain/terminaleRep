def inverse (chaine):
    if len(chaine)==0:
        return ""
    return inverse(chaine[1:])+chaine[0]
print(inverse ("hello"))
