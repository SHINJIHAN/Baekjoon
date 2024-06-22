N = int(input())
max_prize = 0

for _ in range(N):
    A, B, C = map(int, input().split())

    if A==B==C:
        prize = 10000 + A*1000

    elif A==B or A==C:
        prize = 1000 + A*100

    elif B==C:
        prize = 1000 + B*100
    
    else:
        prize = max(A, B, C)*100

    max_prize = max(max_prize, prize)        

print(max_prize)