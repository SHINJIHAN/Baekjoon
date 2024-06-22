# 테스트 케이스 횟수
T = int(input())
for _ in range(T):
    
    # 술 소비량 리스트
    total_alcohol=[]
    
    # 학교 숫자
    N = int(input())
    
    for _ in range(N):
        un, al = input().split()
        al = int(al)
        total_alcohol.append((un, al))
    
    # 술 소비가 가장 많은 학교의 이름을 출력
    max_alcohol = max(total_alcohol, key=lambda x: x[1])
    print(max_alcohol[0])
