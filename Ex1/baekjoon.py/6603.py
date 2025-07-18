printed = False
while True:
    S = list(map(int, input().split()))
    if len(S) == 1 and S[0] == 0:
        break

    K = S[0]
    S = S[1:]

    if printed:
        print()
    printed = True

    for i in range(K - 5):
        for j in range(i + 1, K - 4):
            for k in range(j + 1, K - 3):
                for h in range(k + 1, K - 2):
                    for n in range(h + 1, K - 1):
                        for m in range(n + 1, K):
                            answer = [S[i], S[j], S[k], S[h], S[n], S[m]]
                            print(' '.join(map(str, answer)))