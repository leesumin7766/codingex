S = int(input())

count = 0
i = 1
while S >= i:
    S -= i
    count += 1
    i += 1


print(count)