def pgcd(a, b):
    if b==0:
        return a
    else:
        return pgcd(b,a%b)

def simple(a,b):
    nb=pgcd(a,b)
    print(a,b,",le pgcd est",k)
    return a//k,b//k

print(simple(21,15))

