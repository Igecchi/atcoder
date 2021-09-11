a = "abcdefghijklmnopqrstuvwxyz"
P_list = map(int, input().split())

ans = []
for P in P_list:
    ans.append(a[P-1])
print("".join(ans))