N = int(input())

for i in range(N, 0, -1):
    spaces = N - i
    print(" " * spaces + "*" * (2 * i - 1))