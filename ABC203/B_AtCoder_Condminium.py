N, K = map(int, input().split())

ans = 0
# for n in range(1, N+1):
#     for k in range(1, K + 1):
#         ans += 100 * n + k

for n in range(1, N+1):
    ans += (100 * n * 2 + 1 + K) * K // 2

print(ans)