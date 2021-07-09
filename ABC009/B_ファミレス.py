## 2番目に高い価格を表示する
import sys
N = int(input())
a_list = list(map(int, sys.stdin.readlines()))

a_list = sorted(a_list)

max_a = a_list[-1]
for i in range(1, N+1):
    if a_list[-i] < max_a:
        print(a_list[-i])
        sys.exit()

