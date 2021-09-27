def main():
    import sys
    # 再帰回数上限を10 ** 9回に設定
    sys.setrecursionlimit(10 ** 9)
    
    N = int(input())
    A_list = tuple(map(int, sys.stdin.readline().split()))
    X = int(input())
    
    A_sum = sum(A_list)
    
    count = 0
    if X > A_sum:
        tmp = X // A_sum
        count += tmp * N
        new_X = X - tmp * A_sum
        for a in A_list:
            count += 1
            new_X -= a
            if new_X < 0:
                print(count)
                sys.exit()
    else:
        for a in A_list:
            count += 1
            new_X -= a
            if new_X < 0:
                print(count)
                sys.exit()

main()