# 현재 시각 입력
current_hour, current_minute, current_second = map(int, input().split())

# 요리에 필요한 시간 입력
cooking_time = int(input())

# 전체 초 계산
total_seconds = current_hour * 3600 + current_minute * 60 + current_second

# 요리에 필요한 시간 + 현재 시각
end_total_seconds = total_seconds + cooking_time

# 끝나는 시각 계산
end_hour = (end_total_seconds // 3600) % 24
end_minute = (end_total_seconds // 60) % 60
end_second = end_total_seconds % 60

# 결과 출력
print(end_hour, end_minute, end_second)