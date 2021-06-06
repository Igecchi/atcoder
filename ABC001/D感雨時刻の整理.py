#https://atcoder.jp/contests/abc001/tasks/abc001_4
#一部AC通らず

import sys
N = int(sys.stdin.readline())
list_a = [sys.stdin.readline().rstrip() for _ in range(N)]

list_a.sort()

new_list = []
#雨を直前・直後の5分単位の時刻に丸める
for i in range(N):
    s_keta_1 = int(list_a[i][3])
    e_keta_1 = int(list_a[i][-1])
    
    #直前の5分単位に丸める
    if s_keta_1 < 5:
        new_list.append(int(list_a[i][:3] + "0"))
    else:
        new_list.append(int(list_a[i][:3] + "5"))
    
    #直後の5分単位に丸める(繰り上げに注意する)
    if e_keta_1 == 0:
        new_list.append(int(list_a[i][-4:-1] + "0"))
    elif e_keta_1 <= 5:
        new_list.append(int(list_a[i][-4:-1] + "5"))
    else:
        tmp = int(list_a[i][-2]) + 1
        if tmp == 6:
            tmp_2 = int(list_a[i][-3]) + 1
            if tmp_2 == 10:
                tmp_2 = 0
                new_list.append(int(str(int(list_a[i][-4]) + 1) + "000"))
            else:
                new_list.append(int(list_a[i][-4:-3] + str(tmp_2) + "00"))
        else:
            new_list.append(int(list_a[i][-4:-2] + str(tmp) + "0"))

ans_list = [new_list[0], new_list[1]]
flag = 0
#重複処理を行う
for j in range(1, N):
    if new_list[(j-1)*2] <= new_list[j*2] <= new_list[(j-1)*2 + 1]:
        if new_list[(j-1)*2 + 1] < new_list[(j*2) + 1]:
            ans_list[flag*2 + 1] = new_list[(j*2) + 1]
    else:
        flag += 1
        ans_list.append(new_list[j*2])
        ans_list.append(new_list[(j*2) + 1])

# print(new_list)
# print(ans_list)

for k in range(len(ans_list)//2):
    print("{:0=4}".format(ans_list[k*2]) + "-" + "{:0=4}".format(ans_list[(k*2) + 1]))