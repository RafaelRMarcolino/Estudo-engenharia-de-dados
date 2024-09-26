#Using the following table, write a program that reads a code and the amount 
# of an item. After, print the value to pay. This is a very simple program 
# with the only intention of practice of selection commands.

#Input
#The input file contains two integer numbers X and Y. X is the product 
# code and Y is the quantity of this item according to the above table.

#Output
#The output must be a message "Total: R$ " followed by the total value to be paid,
# with 2 digits after the decimal point.


print('********************************')
print('CODE   SPECIFICATION      PRICE')
print('1     Cachorro-quente    R$4,50')
print('2        X-salada        R$4,50')
print('3        X-Bacon         R$4,50')
print('4     Torrada Simples    R$4,50')
print('5      Refrigerente      R$4,50')
print('********************************')

para = False
total = 0.0

while(para != True):
    
    print('Faça seu pedido (0) para finalizar')
    x = int(input())
     
    if(x == 1):
        valor = 4.50
        print(valor, 'valor')
    
    elif(x == 2):
        valor = 4.90
        print(valor, 'valor')
        
    elif(x == 0):
        fimPedido = True
        break

    
    total += valor    
    
print(fimPedido, ' fimPedido ')
print('total de tudo %.2lf' %total)
    
    