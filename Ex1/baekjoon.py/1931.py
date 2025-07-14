N = int(input())

answer = 0
end_time = 0
meetings = [tuple(map(int, input().split())) for _ in range(N)]

meetings.sort(key = lambda x: (x[1], x[0]))
for i,j in meetings :
    if i >= end_time :
        answer += 1
        end_time = j

print(answer)