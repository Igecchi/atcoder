import sys
S = input()
T = input()
if S == T:
    print("Yes")
    sys.exit()
for s in range(len(S)-1):
    tmp = S[:s] + S[s+1] + S[s] + S[s+2:]
    if tmp == T:
        print("Yes")
        sys.exit()
print("No")