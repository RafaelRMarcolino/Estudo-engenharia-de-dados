import random 

#cubo [12][12]
matrix = [[random.randint(0, 100) for i in range(12)] for _ in range(12) ]

for linha in matrix:
    print(linha)


#cubo [12][12][12]

matrix3 = [[[random.randint(0, 1000)  for _ in range(12)  ] 
             for _ in range(12) ] for _ in range(12)]


for i in range(12):
    print(f"camada {i}")
    for j in range(12):
        print(matrix3[i][j])
    print()


cubo4 = [[[0 for _ in range(12)] for _ in range(12)] for _ in range(12)]
for k in range(12):
    for i in range(12):
        for j in range(12):
            print(cubo4[k][i][j], end=' ')
        print()
    print()