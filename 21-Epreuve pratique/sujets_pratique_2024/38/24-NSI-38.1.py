def indices_maxi(lst):
    max = lst[0]
    indices = []
    for i in range(len(lst)):
        if max < lst[i]:
            max = lst[i]
    for j in range(len(lst)):
        if lst[j] == max:
            indices.append(j)
    return (max,indices)

print(indices_maxi([1, 5, 6, 9, 1, 2, 3, 7, 9, 8]))