N = int(input())

people = []
for _ in range(N) :
    people.append(tuple(map(int, input().split())))

rank = []

for i in range(N) :
    ranks = 1
    for j in range(N) :
        if i != j :
            if people[j][0] > people[i][0] and people[j][1] > people[i][1] :
                ranks += 1
    rank.append(ranks)
        
print(*rank)    