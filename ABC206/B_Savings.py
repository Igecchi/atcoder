N = int(input())

count = 0
def c(count):
    count += 1
    return count

c_sum = 0
while N > c_sum:
    count = c(count)
    c_sum += count

print(count)

_INPUT_ = '''
100128
'''

_OUTPUT_ = '''
447
'''