#Read three integers and sort them in ascending order. After, print these 
# values in ascending order, a blank line and then the values in the sequence as they were readed.

#Input
#The input contains three integer numbers.

#utput
#Present the output as requested above.

x, y, z = list(map(int, input().split()))

lista = [x, y, z]

lista.sort() 

print(lista[0])
print(lista[1])
print(lista[2])

print("")

print(x)
print(y)
print(z)