# 테스트 케이스 입력
T = int(input())

# 각 테스트 케이스 처리
for _ in range(T):
    # 2가지 문자열 입력 및 분할
    R, S = input().split()
    # R을 정수형으로 변환
    R = int(R)
    
    # 문자열S에 각 문자를 R만큼 곱한 값을 P에 저장
    P = ''.join([char * R for char in S])
    
    print(P)