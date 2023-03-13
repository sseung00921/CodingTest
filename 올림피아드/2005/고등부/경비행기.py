import sys;
import math;
from collections import deque;
input = sys.stdin.readline;

INF = int(1e9);
n, k = map(int, input().split());
Graph = [[INF] * (n + 2) for _ in range(n + 2)];
Poses = [];
Poses.append((0, 0));
Poses.append((10000, 10000));
for i in range(n) :
    r, c = map(int, input().split());
    Poses.append((r, c));

for i in range(n + 2) :
    for j in range(i + 1, n + 2) :
        dist = math.ceil(abs((Poses[i][0] - Poses[j][0])**2 + abs(Poses[i][1] - Poses[j][1])**2)**(1/2)/10);
        Graph[i][j] = dist;
        Graph[j][i] = dist;

def check(mid) :
    visited = [False] * (n + 2);
    visited[0] = True;
    q = deque([(0, 0)]);
    while q :
        now, cnt = q.popleft();
        if now == 1 :
            return True;
        if cnt >= k + 1 :
            continue;
        for next in range(len(Graph[now])) :
            if Graph[now][next] > mid :
                continue;
            if visited[next] :
                continue;
            visited[next] = True;
            q.append((next, cnt + 1));
    return False


left = 0; right = 1415;
while left <= right :
    mid = (left + right) // 2
    if check(mid) :
        right = mid - 1;
    else :
        left = mid + 1
print(left);