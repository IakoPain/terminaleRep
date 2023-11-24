def genereDecrementation(n):
    if n==0:
        return [0]
    else:
        return [n]+genereDecrementation(n-1)
print(genereDecrementation(10))
