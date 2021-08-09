N = list(input())

for _ in range(len(N)):
  if N[-1] == "0":
    N = N[:-1]
  else:
    break

opposit_list = []
for i in range(1, len(N)+1):
    opposit_list.append(N[-i])

if N == opposit_list:
    print("Yes")
else:
    print("No")