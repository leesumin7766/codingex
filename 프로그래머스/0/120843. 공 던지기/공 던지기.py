def solution(numbers, k):
    answer = 0
    loc = 1
    for i in range(k-1) :
        if loc == len(numbers) - 1 :
            loc = 1
        elif loc == len(numbers) :
            loc = 2
        else :
            loc += 2
    return loc