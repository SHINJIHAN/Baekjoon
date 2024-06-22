# 테스트 케이스의 수
T = int(input())

for _ in range(T):
    
    # 선수의 수
    p = int(input())
    
    # 선수 정보를 저장할 리스트
    players = []
    
    
    for _ in range(p):
        price, name = input().split()
        price = int(price)
        players.append((price, name))
        
    # 최대 가격 선수 정보 찾기
    max_price = max(players)
    
    print(max_price[1])