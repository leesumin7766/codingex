N, K = map(int, input().split())
coins = [int(input()) for _ in range(N)]

answer = 0
for coin in reversed(coins):
    if K >= coin:
        answer += K // coin
        K %= coin

print(answer)