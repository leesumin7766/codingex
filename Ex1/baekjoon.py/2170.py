N = int(input())

answer = 0
end_point = -1000000000
length = [tuple(map(int, input().split())) for _ in range(N)]

length.sort()
for x, y in length :
    if x >= end_point :
        answer += y - x
        end_point = y
    else :
        if y > end_point :
            answer += y - end_point
            end_point = y

print(answer)