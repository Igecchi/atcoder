tmp = input()

#2文字以上の場合は、一文字減らした文字を表示する
if len(tmp) >= 2:
    print(tmp[:-1])

#1文字の場合は、aならば-1、それ以外ならaを表示する
else:
    if tmp == "a": print(-1)
    else: print("a")