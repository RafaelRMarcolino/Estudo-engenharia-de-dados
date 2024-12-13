# Given an integer, , and  space-separated integers as input, create a tuple, t , of those  integers. Then compute and print the result of .

# Note: hash() is one of the functions in the __builtins__ module, so it need not be imported.

# Input Format

# The first line contains an integer, , denoting the number of elements in the tuple.
# The second line contains  space-separated integers describing the elements in tuple .

tup = ()
n = int(input())

for _ in range(n):
    tup = input().split()
    tup1 = tuple(tup)
    
    print(hash(tup1))
