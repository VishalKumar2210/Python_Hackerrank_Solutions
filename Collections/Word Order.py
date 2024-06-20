from collections import Counter

integer1 = int(input())
lst = [list(map(str, input().split())) for _ in range(integer1)]

words = [x[0] for x in lst]

print(len(Counter(words).keys()))
val = list(Counter(words).values())
listToStr = ' '.join([str(elem) for elem in val])
print(listToStr)