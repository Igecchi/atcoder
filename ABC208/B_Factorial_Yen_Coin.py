#もう少しスマートにやる方法あり
import sys
P = int(input())

# money_list = [1]
# for i in range(2, 11):
#     money_list.append(money_list[i-2] * i)
# print(money_list)
# money_list = [1, 2, 6, 24, 120, 720, 5040, 40320, 362880, 3628800]

count = 0
while 1:
    if P < 720:
        if P < 6:
            if P == 0:
                print(count)
                sys.exit()
            if P == 1 or P == 2: # Pが1, 2となるとき
                count += 1
                print(count)
                sys.exit()
            else: # 3 <= P <6となるとき
                P -= 2
                count += 1
        else: # 6 <= P < 720となるとき
            if 6 <= P < 24:
                P -= 6
                count += 1
            elif 24 <= P <120:
                P -= 24
                count += 1
            elif 120 <= P < 720:
                P -= 120
                count += 1
    else:
        if 720 <= P < 5040:
            P -= 720
            count += 1
        elif 5040 <= P < 40320:
            P -= 5040
            count += 1
        elif 40320 <= P < 362880:
            P -= 40320
            count += 1
        elif 362880 <= P < 3628800:
            P -= 362880
            count += 1
        else:
            P -= 3628800
            count += 1