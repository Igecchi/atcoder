N = int(input())

#一つ目の段ボールを追加
all_list = [[int(input())]] 

#残りn-1個の段ボールを重ねる
for i in range(N-1):
  new_bool = True
  new_num =int(input())
  for j in range(len(all_list)):
    tmp = all_list[j][-1]
    if tmp >= new_num:
      all_list[j].append(new_num)
      break
    else:
      if j == len(all_list)-1:
        all_list.append([new_num])

print(len(all_list))