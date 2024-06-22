T = int(input())

for _ in range(T):
    result = input()
    score = 0
    consecutive = 0
    
    for i in range(len(result)):
        if result[i] == 'O':
            consecutive += 1
            score += consecutive
        else:
            consecutive = 0
    
    print(score)
