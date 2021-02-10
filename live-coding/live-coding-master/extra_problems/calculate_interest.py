"""
Given principal (p),
annual interest rate (r),
time in years (t)

calculate the new total

example
p = 10000
r = .0025
t = 25

total = 10644.11
"""

def compound_interest(p, r, t):
    total = p
    for i in range(0,25):
        total += (total * r)

    return total

print(compound_interest(10000, .0025, 25))