import math
N = int(input())

ans = math.floor(N * 1.08)
if ans < 206:
    print("Yay!")
elif ans == 206:
    print("so-so")
else:
    print(":(")

_INPUT_ = '''
191
'''

_OUTPUT_ = '''
so-so
'''