N = int(input())
answer = 0

for i in range(N) :
    S = input()
    seen  = set()
    group = True
    
    for j in range(len(S)) :
        if S[j] in seen :
            if S[j] != S[j-1] :
                group = False
                break
        seen.add(S[j])
        
    if group == True :
        answer += 1

print(answer)