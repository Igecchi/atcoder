tmp_list = []
for _ in range(4):
    tmp_list.append(input())
    
if len(set(tmp_list)) == 4:
    print("Yes")
else:
    print("No")