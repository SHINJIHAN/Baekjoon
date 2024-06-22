T = int(input())

for _ in range(T):
    # 연세대와 고려대 변수 정의
    yonsei_score = 0
    korea_score = 0
    
    # 각 회의 연세대와 고려대 득점 입력
    for i in range(9):
        A, B = map(int, input().split())
        
        # 득점 계산
        yonsei_score += A
        korea_score += B
    
    # 승부 결과 판단 및 출력
    if yonsei_score > korea_score:
        print("Yonsei")
    elif yonsei_score < korea_score:
        print("Korea")
    else:
        print("Draw")