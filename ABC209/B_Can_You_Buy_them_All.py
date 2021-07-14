import math
N, X = map(int, input().split())
A_list = list(map(int, input().split()))

check = sum(A_list) - math.floor(N/2)
if check <= X:
    print("Yes")
else:
    print("No")