T = int(input())

for i in range(1, T+1):
    A, B = map(int, input().split())
    k=A+B
    print('Case #{}: {}'.format(i,k))