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

# tmp_sum = sum(map(int, list(str(i)))) #こっちの方がスマート！

#参考回答（https://atcoder.jp/contests/abc083/submissions/1899403）
#10ごとにリセットする
# n, a, b = (int(x) for x in input().split())
# c = 0
# sum = 0
# for i in range(1, n+1):
#   c += 1
#   if a <= c <= b:
#     sum += i
#   while i%10 == 9:
#     c -= 9
#     i //= 10
# print(sum)