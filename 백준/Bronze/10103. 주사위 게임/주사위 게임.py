N = int(input())

창영의_점수 = 100
상덕의_점수 = 100

for i in range(N):
    창영, 상덕 = map(int, input().split())
    
    if 창영 > 상덕:
        상덕의_점수 -= 창영
        
    elif 창영 < 상덕:
        창영의_점수 -= 상덕
        
print(창영의_점수)
print(상덕의_점수)
    