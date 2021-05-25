N, L = list(map(int, input().split())) #横, 縦
# print(N, L)
c_list = list(i for i in range(N))
# print(c_list)

amida = []
for i in range(L+1):
  amida.append(input())#高橋くん
  # print(amida)
  for j in range(N-1):
    if amida[i][2 *j+1] == "-":
      c_list[j], c_list[j+1] = c_list[j+1], c_list[j]
  # print(c_list)

position = amida[L].index("o")
# print(position)

print(c_list[position//2] + 1)

