N = int(input())

#昇順でリスト化し、後のforループの計算量を減らせるように仕込む
L_list = sorted(list(map(int, input().split())))
l_len = len(L_list)

count = 0
#三角形の成立条件を満たすLの選び方
for i in range(l_len):
    L_i = L_list[i]
    for j in range(i+1, l_len):
        L_j = L_list[j]
        if L_i != L_j: #LiとLjが異なるかチェックする
            for k in range(j+1, l_len):
                L_k = L_list[k]
                 #LjとLkが異なるか、三角形が成立するかチェックする
                 #斜辺がそれ以外の辺の和より長いと三角形は成立しない
                if L_j != L_k and L_i + L_j > L_k:
                        # print(L_i, L_j, L_k)
                        count += 1

print(count)    