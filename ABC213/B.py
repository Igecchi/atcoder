N = int(input())
A_list = list(map(int,input().split()))
B_list  = sorted(A_list)

# print(B_list)
print(A_list.index(B_list[-2])+1)