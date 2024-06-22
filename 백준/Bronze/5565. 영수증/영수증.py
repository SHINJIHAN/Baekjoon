# 10권의 총 가격 입력
total_price = int(input())

# 책 9권의 가격 리스트
total_book = []

# 책 9권의 가격 입력
for _ in range(9):
    price = int(input())
    if not (0 <= price <= 10000):
        print("가격은 10,000 이하의 양의 정수여야 합니다.")
        break
    total_book.append(price)
    # 총 가격 - 해당 가격 계산
    total_price -= price

# 가격을 읽을 수 없는 책의 가격 출력
print(total_price)
