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

# ##全分岐書く方がやや早い
# S = input()
# count = 0
# if S[0] == 'R':
#     count += 1
#     if S[1] == 'R':
#         count += 1
#         if S[2] == 'R':
#             count += 1
# elif S[1] == 'R':
#     count += 1
#     if S[2] == 'R':
#         count += 1
# elif S[2] == 'R':
#     count += 1
# print(count)

## booleanだけで攻めるとスマート
# S=input()
# a=bool(S[0]=='R')
# b=bool(S[1]=='R')
# c=bool(S[2]=='R')
# if(a and b and c):
#   print(3)
# elif(a and b or b and c):
#   print(2)
# elif(a or b or c):
#   print(1)
# else:
#   print(0)

# ## 単純に一致調べるだけでもOK（見やすい）
# weather=input()
# if "RRR" in weather:
#     print(3)
# elif "RR" in weather:
#     print(2)
# elif "R" in weather:
#     print(1)
# else:
#     print(0)