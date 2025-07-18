N, M = map(int, input().split())

books = list(map(int, input().split()))

minus = []
plus = []
for i in books :
    if i < 0 :
        minus.append(i)
    else :
        plus.append(i)

minus.sort()
plus.sort(reverse = True)
distance = []
for i in range(0, len(minus), M) :
    distance.append(abs(minus[i]))

for i in range(0, len(plus), M) :
    distance.append(abs(plus[i]))

answer = 0
for i in distance :
    answer += i

print(answer * 2 - max(distance))