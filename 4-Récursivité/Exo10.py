def pair(n):
    if n==0:
        return True
    else:
        return impair(n-1)

def impair(n):
    if n==0:
        return False
    else:
        return pair(n-1)

print(pair(2))
print(pair(3))
print(impair(2))
print(impair(3))
