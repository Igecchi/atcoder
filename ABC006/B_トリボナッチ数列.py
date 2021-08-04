N = int(input())
# a1 = 0
# a2 = 0
# a3 = 1
a_list = [0, 0, 1]


if N <= 2:
    print(0)
elif N == 3:
    print(1)
else:
    for i in range(3, N):
        a_list.append(a_list[i-1] + a_list[i-2] + a_list[i-3])

print(a_list[-1]%10007)
#やり直す必要あり↑

## 再度挑戦↓
*a, = [0, 0, 1]
n = int(input())
if n <= 3:
    print(a[n-1])
else:
    for i in range(3, n):
        a.append((a[i-1] + a[i-2] + a[i-3]) % 10007)
    print(a[-1] % 10007)
