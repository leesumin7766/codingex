N, M = map(int, input().split())

N_list = list(map(int, input().split()))

start = 0
end = max(N_list)
answer = 0

while start <= end :
    mid = (start + end) // 2
    total = 0
    
    for i in N_list :
        if i > mid :
            total += i - mid
    
    if total >= M :
        answer = mid
        start = mid + 1
    else :
        end = mid - 1
print(answer)
            
            
