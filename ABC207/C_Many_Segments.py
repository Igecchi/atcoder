import sys
N = int(input())
all_list = [list(map(int, input().split())) for _ in range(N)]

def check(i, all_list):
    t = all_list[i][0]
    l = all_list[i][1] * 10
    r = all_list[i][2] * 10
    if t == 1:
        pass
    elif t == 2:
        r -= 1
    elif t == 3:
        l += 1
    else:
        l += 1
        r -= 1
    return l, r

count = 0
for i in range(N):
    l_1, r_1 = check(i, all_list)
    for j in range(i + 1, N):
        l_2, r_2 = check(j, all_list)
        # if l_1 <= r_2 <= r_1 or l_1 <= l_2 <= r_1:
        if l_1 <= r_2 <= r_1 or l_1 <= l_2 <= r_1 or l_2 <= r_1 <= r_2 or l_2 <= l_1 <= r_2:
            # print(i, j, l_1, r_1, l_2, r_2)
            count += 1
        # print(j)
        
print(count)

_INPUT1_ = '''
19
4 210068409 221208102
4 16698200 910945203
4 76268400 259148323
4 370943597 566244098
1 428897569 509621647
4 250946752 823720939
1 642505376 868415584
2 619091266 868230936
2 306543999 654038915
4 486033777 715789416
1 527225177 583184546
2 885292456 900938599
3 264004185 486613484
2 345310564 818091848
1 152544274 521564293
4 13819154 555218434
3 507364086 545932412
4 797872271 935850549
2 415488246 685203817

'''
_INPUT2_ = '''
102
'''
