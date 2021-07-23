A1, A2, A3 = map(int, input().split())


if A3 - A2 == A2 - A1:
    print("Yes")
elif A1 - A2 == A2 - A3:
    print("Yes")
elif A3 - A1 == A1 - A2:
    print("Yes")
elif A2 - A1 == A1 - A3:
    print("Yes")
elif A2 - A3 == A3 - A1:
    print("Yes")
elif A1 - A3 == A3 - A2:
    print("Yes")
else:
    print("No")