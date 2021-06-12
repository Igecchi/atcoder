K, S = map(int, input().split())

count = 0
## パターン1（計算量O(n^3)）
# for i in range(K+1):
#     for j in range(K+1):
#         for k in range(K+1):
#             if i + j + k == S:
#                 count += 1
#                 break

## パターン1（計算量O(n^2)）
for i in range(K+1):
    for j in range(K+1):
        if 0 <= S - i - j <= K:
            count += 1
            # print(i, j)

print(count)