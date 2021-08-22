import math
N, M = map(int,input().split())
A = tuple(map(int,input().split()))
a_len = len(A)

count = 0
ans_list = []
for i in range(1, M+1):
    is_gcd = True
    for j in range(a_len):
        if math.gcd(A[j], i) == 1:
            pass
        else:
            is_gcd = False
            break
    if is_gcd:
        count += 1
        ans_list.append(i)

print(count)        
for i in ans_list: print(i)