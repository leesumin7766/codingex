N = int(input())
words = set()

for _ in range(N) :
    words.add(input().strip())

word = sorted(words, key=lambda x: (len(x), x))

for i in word :
    print(i)    
