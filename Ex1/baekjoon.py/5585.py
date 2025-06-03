N = int(input())

P = 1000 - N

answer = 0
k_list = [500, 100, 50, 10, 5, 1]

for i in k_list :
    answer += P // i
    P %= i

print(answer)
    