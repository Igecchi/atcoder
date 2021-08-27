import math
import sys
S, T = input().split()
tmp = int(S + T)

count = 0
while True:
    count += 1
    tmp_sqrt = count ** 2
    if tmp_sqrt == tmp:
        print("Yes")
        sys.exit()
    elif tmp_sqrt > tmp:
        print("No")
        sys.exit()