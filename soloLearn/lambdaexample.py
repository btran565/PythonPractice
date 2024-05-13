#named func
def polynomial(x):
    return x**2 + 5*x + 4
print(polynomial(4))

#lambda version
print((lambda x: x**2 + 5*x + 4) (-4))

#filter
nums = [1,2,3,4,5]
res = list(filter(lambda x: x<5, nums))
print(res)