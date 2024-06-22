N = int(input())

for i in range(N):
    spaces = N - i -1
    stars = 2 * i + 1
    print(" " * spaces + '*' * stars)