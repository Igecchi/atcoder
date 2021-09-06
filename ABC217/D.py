L, Q = map(int, input().split())
l_list = [L] * L
for _ in range(Q):
    c, x = map(int, input().split())
    if c == 1: #線xiがある地点で木材を 2 つに切る。
        l_list[x-1]
    else: #線xiを含む木材を選び、その長さを出力する。
        print(l_list[x-1])