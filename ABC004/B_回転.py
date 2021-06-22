first = reversed(input().split())
second = reversed(input().split())
third = reversed(input().split())
fourth = reversed(input().split())

print(" ".join(fourth))
print(" ".join(third))
print(" ".join(second))
print(" ".join(first))

_INPUT_ = '''
. . . .
. o o .
. x x .
. . . .
'''

_OUTPUT_ = '''
. . . .
. x x .
. o o .
. . . .
'''