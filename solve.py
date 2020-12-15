from sympy import *

i1 = Symbol('i1')
u1 = Symbol('u1')
i2 = Symbol('i2')
u2 = Symbol('u2')

i1p = Symbol('i1p')
u1p = Symbol('u1p')
i2p = Symbol('i2p')
u2p = Symbol('u2p')

r1 = Symbol('r1')
r2 = Symbol('r2')

l1 = Symbol('l1')
l1p = Symbol('l1p')

l2 = Symbol('l2')
l2p = Symbol('l2p')

d1 = Symbol('d1')

n = Symbol('n')

solved_value = nsolve([
    sin(i1)/(-l1+r1)-sin(u1)/r1,
    sin(i1)-n*sin(u1),
    u1+u1p-i1,
    l1p-(1+sin(i1p)/sin(u1p))*r1,

    sin(i2)/(-l2+r1)-sin(u2)/r2,
    n*sin(i2)-sin(u2),
    u2+u2p-i2,
    l2p-(1+sin(i2p)/sin(u2p))*r2,

    u2 - u1p,
    l2 - (l1p-d1)
], [l2p])


#solved_value = solve([sin(x) - 0.5+y, y-7], [x, y])
print(solved_value)
