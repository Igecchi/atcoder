K = int(input())
A, B = input().split()

a_10 = 0
new_K = K
for i, a in enumerate(reversed(A)):
    a_10 += (K**i) * int(a)

b_10 = 0
for i,b in enumerate(reversed(B)):
    b_10 += (K**i) * int(b)
print(a_10 * b_10)