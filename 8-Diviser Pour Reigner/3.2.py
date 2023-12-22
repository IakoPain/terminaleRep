def tri_insersion(lst):
    for i in range (0,len(lst)):
        j=i
        while j>0 and lst[j-1]> lst[j]:
            temp=lst[j-1]
            lst[j-1]=lst[j]
            lst[j]=temp
            j-=1
lst=[23,12,4,56,35,57,3,11,6]
tri_insersion(lst)
print(lst)