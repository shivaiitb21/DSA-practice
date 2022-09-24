def fact(n):
    # NOTE THAT in recursion you have to define the base case
    if n==1:
        return 1
    else:
        return n*fact(n-1)

print(fact(5))