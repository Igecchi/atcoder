S = input()

ans_str = ""
for i in range(len(S)):
    tmp = S[-1 - i]
    if tmp == "6":
        ans_str += "9"
    elif tmp == "9":
        ans_str += "6"
    else:
        ans_str += tmp

print(ans_str)
######################################################
# A1, A2, A3 = map(int, input().split())


# if A3 - A2 == A2 - A1:
#     print("Yes")
# elif A1 - A2 == A2 - A3:
#     print("Yes")
# elif A3 - A1 == A1 - A2:
#     print("Yes")
# elif A2 - A1 == A1 - A3:
#     print("Yes")
# elif A2 - A3 == A3 - A1:
#     print("Yes")
# elif A1 - A3 == A3 - A2:
#     print("Yes")
# else:
#     print("No")
######################################################
