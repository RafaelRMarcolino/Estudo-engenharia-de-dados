"""
Write an algorithm to read a value A and a value N. Print the sum of N numbers from A (inclusive).
 While N is negative or ZERO, a new N (only N) must be read. All input values are in the same line.

Input
The input contains only integer values, ​​can be positive or negative.

Output
The output contains only an integer value.
"""

lista = list(map(int, input().split()))
n1 = 'I'
n2 = 0
soma = 0
for i in lista:
    if (n1 == 'I'):
        n1 = i
    else:
        if (i > 0):
            n2 = i
            break

for i in range(n2):
    soma += n1
    n1 += 1

print("%d" % soma)