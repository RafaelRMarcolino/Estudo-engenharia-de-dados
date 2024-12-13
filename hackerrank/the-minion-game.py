def minion_game(string):
    
    # your code goes here
    n = len(string)
    comb = ((n)*(n+1))/2
    count_k = 0
    count_s = 0
    count_k = sum([len(string[i:]) for i in range(len(string)) if string[i] in "AEIOU"])
    count_s = comb - count_k
    
    if count_s == count_k:
        
        print("Draw")
    elif count_s > count_k:
        print("Stuart", int(count_s) )
    else:
        print("Kevin", int(count_k))

    

if __name__ == '__main__':
    s = input()
    minion_game(s)

##################################

def minio_games(string):

    vogais = 'AEIOU'
    n = len(string)
    stuart_score = 0
    kevin_scpre = 0

    for i in range(n):
        if string[i] in vogais:

            print('*******')
            print(string[i])

            kevin_scpre += n - i
            print(f'kevin  point {kevin_scpre}')
            

        else:
            print(string[i])
            stuart_score += n - i
            print(f'stuart point{stuart_score}')
            print('ganhou 2')

    if stuart_score > kevin_scpre:
        print(f'Stuart {stuart_score}')

    elif kevin_scpre > stuart_score:
        print(f'Kevin stuart {kevin_scpre}')

    else:
        print('draw')


minio_games('BANANA')