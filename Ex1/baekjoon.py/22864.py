A, B, C, M = map(int, input().split())

if A > M :
    print(0)
    exit()
    
stress = 0
work = 0
for _ in range(24) :
    if stress + A > M :
        stress -= C
        if stress < 0 :
            stress = 0 
    else :
        stress += A
        work += B
print(work)