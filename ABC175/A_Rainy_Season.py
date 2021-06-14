S = input()

count = 0
ans = 0
for s in S:
    if s == "R":
        count += 1
    else:
        count = 0
    ans = max(count, ans)

print(ans)