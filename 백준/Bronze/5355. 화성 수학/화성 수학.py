# 테스트 케이스의 수
T = int(input())

for _ in range(T):
    # 화성수학식
    formula = input().strip()
    
    # 숫자와 연산자 변수 정의
    num = float(formula.split()[0])
    op = formula.split()[1:]
    
    # 연산 수행
    for i in op:
        if i == '@':
            num *= 3
        elif i == '%':
            num += 5
        elif i == '#':
            num -= 7
 
    print("{:.2f}".format(num))
