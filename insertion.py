a = [14,46,43,27,57,41,45,21,70]

#THis is the insertion sort algorithm
for i in range(1,len(a)):
    for j in range(0,i):
        if a[i]<a[j]:
            a.insert(j, a.pop(i))
    print(a)

print(a)