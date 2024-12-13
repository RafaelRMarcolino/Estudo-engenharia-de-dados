"""
Your program must read an integer X indefinited times (the program must stop when X is equal to zero). For each X print the sequence from 1 to X, 
with one space between each one of these numbers.

PS: Be carefull. Don't leave any space after the last number of each line, otherwise you'll get Presentation Error.

Input
The input file contains many integer numbers. The last one is zero.

Output
For each number N of the input file, one output line must be printed, from 1 to N like the following example. Be careful with blank spaces after the last line number.

"""


while(True):
    n = int(input())
    r = ''
    if(n == 0):
        break
    for i in range(1,n+1):
        r += str(i) + " "
        print(r[:-1])
        


