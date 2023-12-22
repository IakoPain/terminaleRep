def minimum(lst,d,f):
    if d==f:
        return lst[d]
    else:
        m=(d+f)//2
        x=minimum(lst,d,m)
        y=minimum(lst,m+1,f)
        if x<y:
            return x
        else:
            return y

lst=[23,12,4,56,35,57,3,11,6]
print(minimum(lst,0,len(lst)-1))