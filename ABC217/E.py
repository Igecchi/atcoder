from collections import deque
import sys

Q = int(input())
A_queue = deque([])
for _ in range(Q):
    num_list = sys.stdin.readline()
    num = int(num_list[0])
    if num == 1:
        A_queue.append(int(num_list[2]))
    elif num == 2:
        print(A_queue.popleft())
    else:
        A_queue = deque(sorted(tuple(A_queue)))