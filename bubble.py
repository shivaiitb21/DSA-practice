n = int(input())
swapped = False
a = list(map(int,input().split()))

def bubblesort(a):
    n = len(a)

    for i in range(n-1):

        for i in range(n-i-1):

            if a[i] > a[i+1]:
                swapped = True
                a[i],a[i+1] = a[i+1],a[i]

        if not swapped:
            return

a = [39, 12, 18, 85, 72, 10, 2, 18]

print("Unsorted list is,")
print(a)
bubblesort(a)
print("Sorted Array is, ")
print(a)            

