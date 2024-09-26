"""
Write an program that reads two numbers X and Y (X < Y). After this, show a sequence of 1 to y, passing to the next line to each X numbers.

Input
The input contains two integer numbers X (1 < X < 20) and Y (X < Y < 100000).

Output
Each sequence must be printed in one line, with a blank space between each number, like the following example
"""

x, y = list(map(int, input().split()))
cont = 1
for _ in range(1, int(y/x)+1):
    msg = ""
    for _ in range(x):
        msg += str(cont)+" "
        cont+=1
    print(msg[:-1])

