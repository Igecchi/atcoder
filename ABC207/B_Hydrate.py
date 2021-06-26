import math
A, B, C, D = map(int, input().split())
CD = C * D

if CD - B > 0:
    ans = math.ceil(A / (CD - B))
    print(ans)
else:
    print(-1)


_INPUT1_ = '''
6 9 2 3
'''
_INPUT2_ = '''
5 2 3 2
'''

_OUTPUT1_ = '''
-1
'''
_OUTPUT2_ ='''
2
'''