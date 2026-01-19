N = int(input())

answer = 0
imo_cnt = 0
people = set()
for _ in range(N) :
    chat = input()

    if chat == "ENTER" :
        answer += imo_cnt
        imo_cnt = 0
        people.clear()
    else :
        if chat not in people :
            people.add(chat)
            imo_cnt += 1
        else :
            pass

print(answer + imo_cnt)