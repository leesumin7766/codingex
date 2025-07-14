pasta = []
juice = []
for _ in range(3) :
    pasta.append(int(input()))
for _ in range(2) :
    juice.append(int(input()))

pasta.sort()
juice.sort()

answer = (pasta[0] + juice[0]) + ((pasta[0] + juice[0]) / 10)

print(answer)
