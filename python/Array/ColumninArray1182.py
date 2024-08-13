# Your job in this problem is to read a number that is a column of an array where an operation will be performed, 
# an uppercase character, indicating the operation to be performed and all elements of a bidimentional array M[12][12].
# Then, you have to calculate and print the sum or average of all elements within the green area according to the case.
# The following figure illustrates the case when is entered the number 5 to the array column, showing all elements that 
# must be considered in the operation.

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