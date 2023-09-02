import sys;
input = sys.stdin.readline;
from collections import deque;

T = int(input());
INF  = sys.maxsize
d = [[INF, INF, INF, INF, INF] for _ in range(61)]
d[0] = [0, 0, 0, 0, 0];

q = deque([(0, [0, 0, 0, 0, 0])]);
Visited = [0] * 61;
Visited[0] = 1;
while q :
    nowNum, nowArr = q.popleft();
    if nowNum + 60 <= 60 :
        if sum(d[nowNum]) + 1 < sum(d[nowNum + 60]) :
            d[nowNum + 60] = d[nowNum][:]
            d[nowNum + 60][0] += 1;
            q.append((nowNum + 60, d[nowNum + 60]));
        elif sum(d[nowNum]) + 1 == sum(d[nowNum + 60]) :
            tmp = d[nowNum][:]
            tmp[0] += 1;
            if tmp < d[nowNum + 60] :
                d[nowNum + 60] = tmp;
                q.append((nowNum + 60, d[nowNum + 60]));
    if nowNum + 10 <= 60 :
        if sum(d[nowNum]) + 1 < sum(d[nowNum + 10]) :
            d[nowNum + 10] = d[nowNum][:]
            d[nowNum + 10][1] += 1;
            q.append((nowNum + 10, d[nowNum + 10]));
        elif sum(d[nowNum]) + 1 == sum(d[nowNum + 10]) :
            tmp = d[nowNum][:]
            tmp[1] += 1;
            if tmp < d[nowNum + 10] :
                d[nowNum + 10] = tmp;
                q.append((nowNum + 10, d[nowNum + 10]));
    if nowNum - 10 >= 0 :
        if sum(d[nowNum]) + 1 < sum(d[nowNum - 10]) :
            d[nowNum - 10] = d[nowNum][:]
            d[nowNum - 10][2] += 1;
            q.append((nowNum - 10, d[nowNum - 10]));
        elif sum(d[nowNum]) + 1 == sum(d[nowNum - 10]) :
            tmp = d[nowNum][:]
            tmp[2] += 1;
            if tmp < d[nowNum - 10] :
                d[nowNum - 10] = tmp;
                q.append((nowNum - 10, d[nowNum - 10]));
    if nowNum + 1 <= 60 :
        if sum(d[nowNum]) + 1 < sum(d[nowNum + 1]) :
            d[nowNum + 1] = d[nowNum][:]
            d[nowNum + 1][3] += 1;
            q.append((nowNum + 1, d[nowNum + 1]));
        elif sum(d[nowNum]) + 1 == sum(d[nowNum + 1]) :
            tmp = d[nowNum][:]
            tmp[3] += 1;
            if tmp < d[nowNum + 1] :
                d[nowNum + 1] = tmp;
                q.append((nowNum + 1, d[nowNum + 1]));
    if nowNum - 1 >= 0 :
        if sum(d[nowNum]) + 1 < sum(d[nowNum - 1]) :
            d[nowNum - 1] = d[nowNum][:]
            d[nowNum - 1][4] += 1;
            q.append((nowNum - 1, d[nowNum - 1]));
        elif sum(d[nowNum]) + 1 == sum(d[nowNum - 1]) :
            tmp = d[nowNum][:]
            tmp[4] += 1;
            if tmp < d[nowNum - 1] :
                d[nowNum - 1] = tmp;
                q.append((nowNum - 1, d[nowNum - 1]));


for _ in range(T) :
    N = int(input());
    a = N // 60;
    b = N % 60;
    answer = d[b][ : ];
    answer[0] += a;
    print(*answer)