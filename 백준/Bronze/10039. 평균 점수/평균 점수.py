scores = [max(int(input()), 40) for _ in range(5)]

average_score = sum(scores) // 5

print(average_score)