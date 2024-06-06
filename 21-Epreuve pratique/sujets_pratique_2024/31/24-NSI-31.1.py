def multiplication(n1, n2):
    total=0
    if n1>=0 and n2>=0:
        for i in range (0,n1):
         total+=n2
    elif n1<=0 and n2<=0:
        n1=n1-n1-n1
        n2=n2-n2-n2
        for j in range(0,n1):
            total+=n2
    elif n1<=0 and n2>=0:
        n1=n1-n1-n1
        for k in range(0,n1):
            total+=n2
    elif n1>=0 and n2<=0:
        n2=n2-n2-n2
        for l in range(0,n1):
            total+=n2
    return(total)