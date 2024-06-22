K, N, M = map(int, input().split())

# 전체 금액 계산
total_cost = K*N

# 0과 부족한 값 비교
shortage = max(0, total_cost - M)

print(shortage)