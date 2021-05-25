import sys
tmp = sys.stdin
target = list(map(int, tmp.readline().split())) #当選番号
x = int(tmp.readline()) #ボーナス
takahashi = list(map(int, tmp.readline().split())) #高橋くん

count = 0
bonus = False
for t in takahashi:
  if t in target:
    count += 1
  if t == x:
    bonus = True
    
if count < 3:
  print(0)
elif count == 6:
  print(1)
elif count == 5:
  if bonus:
    print(2)
  else:
    print(3)
elif count == 4:
  print(4)
elif count == 3:
  print(5)