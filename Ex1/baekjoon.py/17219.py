N, M = map(int, input().split())
answer = {}
for _ in range(N):
    link, password = input().split()
    answer[link] = password
    
for _ in range(M):
    link = input().strip()
    print(answer[link])

