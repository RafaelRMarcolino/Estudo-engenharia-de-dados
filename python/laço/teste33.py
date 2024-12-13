import random

n = random.randint(1, 30)

if n %2!= 0:
    print('Weird')
    print(f'{n} 1')
    
else:
    
    if n >=2 & n <= 5:
        print('Not Weird')
        print(f'{n} 2')

    elif n >=6 & n <= 20:
        print('Weird') 
        print(f'{n} 3')

    elif n > 20:
        print('Weird') 
        print(f'{n} 4')
    