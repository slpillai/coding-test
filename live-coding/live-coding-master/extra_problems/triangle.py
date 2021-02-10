'''
3 sides of a triangle
a = ?
b = ?
c = ?

you need to write a function that returns True or False.

True if the three integers could touch

False if the three integers could not touch

a = 2
b = 2
c = 2
True

a = 156
b = 10
c = 2
False
'''

def is_triangle(a, b, c):
    if (a + b) > c and (b + c) > a and (c + a) > b:
        return True
    else:
        return False



print(is_triangle(2,2,2))
print(is_triangle(256,2,2))