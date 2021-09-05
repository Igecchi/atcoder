N = int(input())
p_list = list(map(int, input().split()))
q_list = [0] * N

for i in range(N):
    q_list[p_list[i]-1] = i + 1
print(" ".join(map(str, q_list)))