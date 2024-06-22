# 현재 시, 분 입력
current_hour, current_minute = map(int, input().split())

# 추가 분 입력
add_minute = int(input())

# 현재 분 + 추가 시간
total_minutes = current_hour * 60 + current_minute + add_minute

# 새로운 시간 계산
new_hour = total_minutes // 60 % 24
new_minute = total_minutes % 60

print(new_hour, new_minute)
