"""
Read an integer value N. After, read these N values and print a message for each value saying if this value is odd, even,
 positive or negative. In case of zero (0), although the correct description would be "EVEN NULL", because by definition zero is even, your program must print only "NULL", without quotes.

Input
The first line of input is an integer N (N < 10000), that indicates the total number of test cases. Each case is a integer number X (-107 < X <107)..

Output
For each test case, print a corresponding message, according to the below example. All messages must be printed 
in uppercase letters and always will have one space between two words in the same line.


"""

print('Quantas vezes deseja fazer o teste ')
x = int(input())

for y in range(x):
    
    print('Escreva um numero ')
    n = int(input())

    if(n %2==0  ):
        print(f"Numero {n} numero par") 
    else:
        print(f'Numero {n} impar ')

print('Fim do teste')
