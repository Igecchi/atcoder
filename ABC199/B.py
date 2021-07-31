N = int(input())
A_list = map(int, input().split())
B_list = map(int, input().split())

a = max(A_list)
b = min(B_list)
ans = b - a + 1
if ans >= 1:
    print(ans)
else:
    print(0)