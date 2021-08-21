import sys
N = int(input())
count = 0
if N == 1:
    print(0)
    sys.exit()

is_on = True
while is_on:
    N //= 2
    count += 1
    if N < 2:
        is_on = False
print(count)