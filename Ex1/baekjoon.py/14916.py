n = int(input())
answer = 0

while n >= 0:
    if n % 2 == 0:
        print(answer + (n // 2))
        break
    n -= 5
    answer += 1
else:
    print(-1)
        