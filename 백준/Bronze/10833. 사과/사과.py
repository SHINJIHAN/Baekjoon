# 학교의 수 입력
N = int(input())

# 남는 사과의 총 개수 초기화
total_remainder = 0

for _ in range(N):
    students, apples = map(int, input().split())
    
    # 남는 사과의 개수 계산하여 총 개수에 더함
    total_remainder += apples % students

print(total_remainder)
