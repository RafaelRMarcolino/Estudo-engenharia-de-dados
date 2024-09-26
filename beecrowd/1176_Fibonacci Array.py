"""
Write a program that reads a number and print the Fibonacci number corresponding to this read number.
 Remember that the first elements of the Fibonacci series are 0 and 1 and each next term is the sum of the two preceding it.
   All the Fibonacci numbers calculated in this program must fit in a unsigned 64 bits number.

Input
The first line of the input contains a single integer T, indicating the number of test cases. Each test case contains a single 
integer N (0 ≤ N ≤ 60), corresponding to the N-th term of the Fibonacci series.

Output
For each test case in the input, print the message "Fib(N) = X", where X is the N-th term of the Fibonacci series.

"""


new_list=[0,1]
a = 0
t = 1

for i in range(60):
    tnp = t + a
    new_list.append(tnp)
    a = t
    t=tnp

n = int(input())
for i in range(n):
    valor = int(input())
    print('Fib(%d) = %d' %(valor,new_list[valor]))