import sys
a = [64, 25, 12, 22, 11]
n = len(a)

for i in range(n):
    minid = i
    
    for j in range(i+1, n):
        if a[minid] > a[j]:
            minid = j
        
    a[i],a[minid] = a[minid], a[i]

    print(a)
print(a)