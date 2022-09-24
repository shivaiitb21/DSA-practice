# Lambda function
b = lambda x: "Even" if x%2==0 else "Odd"
print(b(5))

print()

# map function
l = [1,2,3]
print(list(map(lambda x:x*2, l)))

print()

#Filter function
print(list(filter(lambda x: x>2, l)))

