from collections import deque
S = input()

words = deque()
answer = []
tag = False

for i in S :
    if i == '<' :
        while answer :
            answer.append(words.pop())
        tag = True
        words.append(i)
    elif i == '>' :
        tag = False
        words.append(i)
        
    elif i == ' ':
        answer.append(words)
        words.clear()
    if tag == False :
        words.appendleft(i)
    elif tag == True :
        words.append(i)
    

print(*answer)