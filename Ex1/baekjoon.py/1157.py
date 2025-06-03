import collections

S = input()

S  = S.upper()

counter = collections.Counter(S)

max_counter  = max(counter.values())

answer = [char for char, count in counter.items() if count == max_counter]

print("?" if len(answer) > 1 else answer[0])