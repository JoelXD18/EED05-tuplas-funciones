lista = [0, 1, 2]
dic = {0:'A', 1:'B'}
tupla = (1, 2, 3)
print(type(tupla))

for t in tupla:
    print("t: ", t)


for l in lista:
    print("l: ", l)

print("\n")

for d in dic.values(): #dic.keys para solo imprimir los indices (0 y 1)
    print("d: ", d)

#caracterisitcas tuplas

print("l[0]: ", lista[0])

print("t[0]: ", tupla[0])

