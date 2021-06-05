##途中
m = int(input())

if m < 1000:
    print("00")
elif m <= 5000:
    ans = m // 1000
    if not ans:
        pass
    else:
        print(ans * 10)
else:
    pass