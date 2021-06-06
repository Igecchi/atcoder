from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_EVEN
Deg, Dis = list(map(int, input().split()))

Dir_list = ["N", "NNE", "NE", "ENE", "E", "ESE", "SE", "SSE", "S", "SSW", "SW", "WSW", "W", "WNW", "NW", "NNW", "N"]
W_list = [0.0, 0.3, 1.6, 3.4, 5.5, 8.0, 10.8, 13.9, 17.2, 20.8, 24.5, 28.5, 32.7]

Deg_n = Deg/10
W_tmp = Decimal(str(Dis/60)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)

for i in range(0, 17):
    tmp = 11.25 + (22.50 * i)
    if Deg_n < tmp:
        Dir = Dir_list[i]
        break

W = 0
for j in range(12, 0, -1):
    # print(j)
    W_p = W_list.pop()
    if W_tmp >= W_p - 0.01:
        W = j
        break

if not W:
    Dir = "C"

print(Dir, W)
