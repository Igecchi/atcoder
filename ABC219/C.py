## My answer
alphabet = "abcdefghijklmnopqrstuvwxyz"
X = input()
N = int(input())
ans_dict = {}
for _ in range(N):
    word = input()
    tmp = ""
    for w in word:
        tmp += alphabet[X.index(w)]
    ans_dict[tmp] = word
    
# print(ans_dict)
# dict_sorted = sorted(ans_dict.items(), key=lambda x:x[0])
# print(dict_sorted)
for y in sorted(ans_dict.items(), key=lambda x:x[0]): print(y[1])


## Other answer
X, N, *S = open(0).read().split()
# print(X)
# print(S)
# print(dict(zip(X, range(26))))
table = str.maketrans(dict(zip(X, range(26))))
# print(table)
S.sort(key=lambda s: s.translate(table))

for s in S:
    print(s)