N = int(input())
card_list = [1, 2, 3, 4, 5, 6]

## TLEとなるコード
# for i in range(N):
#     tmp = i % 5
#     card_list[tmp], card_list[tmp + 1] = card_list[tmp + 1], card_list[tmp]
    
# print("".join(map(str, card_list)))


## 正答
N_mod_30 = N % 30
for i in range(N_mod_30):
    tmp = i % 5
    card_list[tmp], card_list[tmp + 1] = card_list[tmp + 1], card_list[tmp]
    
print("".join(map(str, card_list)))


_INPUT_ = '''
100000000
'''

_OUTPUT_ = '''
345612
'''