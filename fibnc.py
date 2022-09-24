def fib(m):
    if m==0 or m==1:
        return 1
    else:
        return fib(m-1) + fib(m-2)

print(fib(5))

# Not so efficient code using recursion