import collections
N = int(input())
A_list = map(int, input().split())

count = N * (N-1) // 2
c = collections.Counter(A_list)

for c_num in c.values():
    count -= c_num * (c_num-1) // 2

print(count)

## 下記だとTLEとなる
# N = int(input())
# A_list = list(map(int, input().split()))
# count = 0

# for i in range(N):
#     for j in range(i, N):
#         if A_list[i] != A_list[j]:
#             count += 1
        
# print(count)

_INPUT_ = '''
20
7 8 1 1 4 9 9 6 8 2 4 1 1 9 5 5 5 3 6 4
'''

_OUTPUT_ = '''
173
'''