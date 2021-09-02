W = input()
# W = W.replace("a", "")
# W = W.replace("i", "")
# W = W.replace("u", "")
# W = W.replace("e", "")
# W = W.replace("o", "")
# print(W)

boin = ("a", "i", "u", "e", "o")
for x in boin:
    W = W.replace(x, "")
print(W)