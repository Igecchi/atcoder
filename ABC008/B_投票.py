import sys
import collections

N = int(input())
tmp = list(input() for _ in range(N))

c = collections.Counter(tmp)
print(c.most_common()[0][0])