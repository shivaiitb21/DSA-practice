import sys

sys.setrecursionlimit(1500000)

def merge_sort(a):
    la = a[:len(a)//2]
    ra = a[len(a)//2:]

    merge_sort(la)
    merge_sort(ra)

    i = 0 #Left array index
    j = 0 #right array index
    k = 0 #SOrted array index

    while i<len(la) and j<len(ra):
        if la[i] < ra[j]:
            a[k] = la[i]
            i += 1
        else:
            a[k] = ra[j]
            j += 1
        k += 1

    #Now if some elements in left or right array are remaining
    #Transfer thme to the sorted array

    while i<len(la):
        a[k] = la[i]
        i += 1
        k += 1
    while j<len(ra):
        a[k] = ra[j]
        j += 1
        k += 1

def printList(a):
    for i in range(len(a)):
        print(a[i], end=" ")
    print()


if __name__ == '__main__':
    a = [6, 5, 12, 10, 9, 1]

    merge_sort(a)

    print("Sorted array is: ")
    printList(a)


