from collections import deque;

import sys;
input = sys.stdin.readline;

n, l = map(int, input().split());
data = list(map(int, input().split()));

q = deque([]);
answer = [];
for i in range(n) :
    while q and data[i] < q[-1][0] :
        q.pop();
    while q and i - l + 1 > q[0][1] :
        q.popleft();
    q.append((data[i], i));
    answer.append(q[0][0]);

print(*answer);