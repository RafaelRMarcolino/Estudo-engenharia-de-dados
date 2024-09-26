my_list = [1, 2, 3, 4, 5]
print(my_list[3:])  # Saída: [3, 4, 5]

my_string = "Python é incrível"
print(my_string[9:])  # Saída: incrível

print('Com passos')
my_string = "abcdefgh"
print(my_string[2::2])  # Saída: ceg

print('Com índices negativos (contando de trás para frente)')
my_list = [1, 2, 3, 4, 5]
print(my_list[-2:])  # Saída: [3, 4, 5]

#Lista invertida em python
s = "Python"
x = s[::-1]
print(x)  # Saída: "nohtyP"


# Definindo uma linha do padrão de Rangoli como exemplo
linha = "ABCDE"

# Definindo a largura desejada para a linha centralizada
largura = 30

# Imprimindo a linha centralizada
print(linha.center(largura, '*'))