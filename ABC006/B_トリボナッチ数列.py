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