import sys
N = int(input())
A_list = list(map(int, input().split()))

for i in range(1, N+1):
    if i not in A_list:
        print("No")
        sys.exit()

print("Yes")

