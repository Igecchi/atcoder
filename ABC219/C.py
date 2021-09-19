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