while True:
    N = int(input())
    
    # N = -1일 때, 종료
    if N == -1:
        break
    
    # 약수의 리스트
    divisors = []
    for i in range(1, N):
        
        # N의 약수이면,
        if N % i == 0:
            # 리스트에 저장
            divisors.append(i)

    # 약수의 합이 N이면, 구문 출력
    if sum(divisors) == N:
        print(f"{N} = {' + '.join(map(str, divisors))}")
    else:
        print(f"{N} is NOT perfect.")
