S = input()

stick = []
razer = 0
answer = 0

for i in range(len(S)) :
    if S[i] == '(' :
        stick.append(i)
    elif S[i] == ')' :
        stick.pop()
        if S[i-1] == '(' :
            answer += len(stick)
        else :
            answer += 1

print(answer)
        