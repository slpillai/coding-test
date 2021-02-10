'''
given x

print the x numbers of the fibonnacci sequence starting with 0, and 1

x = 5
0
1
1
2
3
'''


# Procedural
def fibon(x):
    fib1 = 0
    fib2 = 1
    print(fib1)
    print(fib2)
    for i in range(2,x):
        fib3 = fib1+fib2
        print(fib3)
        fib1 = fib2
        fib2 = fib3


fibon(5)
