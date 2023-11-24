def fractionelle(n):
    print("fract",n)
    if n==0:
        return 1
    else:
        return n*fractionelle(n-1)

print(fractionelle(5))