def x2(a):
    return 2*a

def x2x3(a):
    return 2*a,3*a

print("x2(a): ", x2(2))

print("x2(a) y x3(a): ", x2x3(2))

a=2

a2, a3 = x2x3(a)
print("a2: ", a2, " a3: ", )

