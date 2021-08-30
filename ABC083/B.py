N, A, B  = map(int,input().split())

ans = 0
for i in range(1, N+1):
    tmp = str(i)
    tmp_sum = 0
    for j in range(len(tmp)):
        tmp_sum += int(tmp[j])
    if A <= tmp_sum <= B:
        ans += i
print(ans)