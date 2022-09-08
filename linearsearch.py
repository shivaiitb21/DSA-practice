def search(arr, N, x):
 
    for i in range(0, N):
        if (arr[i] == x):
            print (i)
    return(-1)

arr = [1,2,3,5,6]
N = len(arr)
x = 2

search(arr, N, x)
