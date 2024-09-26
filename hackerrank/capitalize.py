# You are asked to ensure that the first and last names of people begin with a capital letter in their passports.
#  For example, alison heck should be capitalised correctly as Alison Heck.


# Given a full name, your task is to capitalize the name appropriately.

# Input Format

# A single line of input containing the full name, .

# Constraints

# The string consists of alphanumeric characters and spaces.
# Note: in a word only the first character is capitalized. Example 12abc when capitalized remains 12abc.

# Output Format

# Print the capitalized string, .

# Sample Input

# chris alan
# Sample Output

# Chris Alan

# jesus de nazare
# maria jose
# cris alan

# list = ['jesus de nazare', 'maria jose', 'cris alan']
# nomes = []
# for i in list:
#    x = i.split(' ')
#    print(x)
#    print('********')
   


# Você pode usar o método capitalize() em conjunto com o método join() para alcançar o resultado desejado. Aqui está como você pode fazer:

# python
# Copiar código
def solve(s):
    ans = s.split(' ')
    ans1 = [i.capitalize() for i in ans]
    return ' '.join(ans1)
    


nomes = ['sergio paulo', 'maria jose', 'cris alan']

nomes_maiuscula = [' '.join([palavra.capitalize() for palavra in nome.split()]) for nome in nomes]

print(nomes_maiuscula)