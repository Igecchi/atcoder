m = int(input())
ans = m // 1000

if m < 100:
    ans = "00"
elif m <= 5_000:
    ans = m // 100
    if ans < 10:
        ans = "0" + f"{ans}"
elif m <= 30_000:
    ans += 50
elif m <= 70_000:
    ans = ((ans - 30) // 5) + 80
else:
    ans = 89

print(ans)