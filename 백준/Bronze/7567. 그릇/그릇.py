arrangement = input()

total_height = 10
for i in range(1, len(arrangement)):
    if arrangement[i]==arrangement[i-1]:
        total_height += 5
    if arrangement[i]!=arrangement[i-1]:
        total_height += 10

print(total_height)        