import random
def lancer(n):
    table=[]
    for i in range(0,n):
        table.append(random.randint(1, 6))
    return (table)

print(lancer(9))
