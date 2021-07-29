N = int(input())
mountain_name = []
mountain_height = []
for _ in range(N):
    S, T = input().split()
    mountain_name.append(S)
    mountain_height.append(int(T))

mouontain_height_asc = sorted(mountain_height)
print(mountain_name[mountain_height.index(mouontain_height_asc[-2])])