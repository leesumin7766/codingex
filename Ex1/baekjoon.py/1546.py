N = int(input())
score = list(map(int,input().split()))
M = max(score)
l_score = []
for i in score :
        i = (i/M) * 100
        l_score.append(i) 

print(sum(l_score)/N)