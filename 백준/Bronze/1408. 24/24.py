# 현재 시간 입력
current_time = input().split(':')
current_hour = int(current_time[0])
current_minute = int(current_time[1])
current_second = int(current_time[2])

# 임무 시작 시간 입력
start_time = input().split(':')
start_hour = int(start_time[0])
start_minute = int(start_time[1])
start_second = int(start_time[2])

# 현재 시간
current_seconds = current_hour * 3600 + current_minute * 60 + current_second

# 임무 시작 시간
start_seconds = start_hour * 3600 + start_minute * 60 + start_second

# 남은 시간 계산
remaining_seconds = (start_seconds + 86400 - current_seconds) % 86400

# 남은 시간을 시, 분, 초로 변환
remaining_hour = remaining_seconds // 3600
remaining_minute = (remaining_seconds % 3600) // 60
remaining_second = remaining_seconds % 60

print('{:02d}:{:02d}:{:02d}'.format(remaining_hour, remaining_minute, remaining_second))
