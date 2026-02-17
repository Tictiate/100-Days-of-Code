def add(*args):
    print(args[1])

    sum = 0
    for n in args:
        sum += n
    return sum

# print(add(3,4,6,2,1,7,4,3))

def calculate(n, **kwargs):
    print(kwargs)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)

calculate(2, add=3, multiply=5)