import sys
N = int(input())
N_list = [input().split() for _ in range(N)]

for i in range(3):
    s = N_list[i][0]
    t = N_list[i][1]
    for j in range(i+1, 3):
        if N_list[j][0] == s:
            if N_list[j][1] == t:
                print("Yes")
                sys.exit()
print("No")