A, B, C = map(int, input().split())

def check(a, b):
    if a < b:
        print("<")
    elif a > b:
        print(">")
    else:
        print("=")

# AとBの絶対値の大小関係を比べる
if C % 2:
    check(A, B)
else:
    A_abs = abs(A)
    B_abs = abs(B)
    check(A_abs, B_abs)
    
