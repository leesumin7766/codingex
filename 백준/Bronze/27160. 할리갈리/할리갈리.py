N = int(input())

cards = {}

for _ in range(N) :
    fruit, number = input().split()
    number = int(number)
    if fruit in cards :
        cards[fruit] += number
    else :
        cards[fruit] = number

answer = "NO"
for fruit in cards :
    if cards[fruit] == 5 :
        answer = "YES"
        break

print(answer)