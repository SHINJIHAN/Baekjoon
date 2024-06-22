H, M = map(int, input().split())

total_M = H*60+M

adjusted_M = (total_M - 45) % 60
adjusted_H = (total_M - 45) // 60 

if adjusted_M < 0:
    adjusted_M = adjusted_M + 60
    
if adjusted_H < 0:
    adjusted_H = (adjusted_H +1) + 23
    
print(adjusted_H, adjusted_M)