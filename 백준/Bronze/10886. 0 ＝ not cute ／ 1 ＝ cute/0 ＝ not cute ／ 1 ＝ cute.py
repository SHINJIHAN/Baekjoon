N = int(input())

votes_0 = 0
votes_1 = 0

for _ in range(N):
    opinion = int(input())
    if opinion == 0:
        votes_0 += 1
    else:
        votes_1 += 1

if votes_1 > votes_0:
    print("Junhee is cute!")
    
elif votes_1 < votes_0:
    print("Junhee is not cute!")