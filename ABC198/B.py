N = list(input())
print(N)

opposit_list = []
for i in range(1, len(N)+1):
    opposit_list.append(N[-i])
print(opposit_list)

#0を入れなくても回文の場合
if N == opposit_list:
    print("Yes")
    