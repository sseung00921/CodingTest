import sys;
input = sys.stdin.readline;
from collections import deque;

M, N = map(int, input().split());
K = int(input());
Info = [];
for _ in range(K) :
    num, x1, y1, x2, y2 = map(int, input().split());
    if x1 == x2 :
        Info.append((num, 0, x1, y1, y2));
    elif y1 == y2 :
        Info.append((num, 1, y1, x1, x2));
sx, sy, dx, dy = map(int, input().split());
Info = [(-1, -1, -1, -1, -1)] + Info;
Info.sort();

def checkIfCanGo(bus1, bus2) :
    num1, dir1, fix1, start1, dest1 = bus1;
    num2, dir2, fix2, start2, dest2 = bus2;
    if dir1 == dir2 :
        if fix1 != fix2 :
            return False;
        if min(start2, dest2) > max(start1, dest1) or min(start1, dest1) > max(start2, dest2) :
            return False;
        return True;
    elif dir1 != dir2 :
        if min(start2, dest2) <= fix1 <= max(start2, dest2) and min(start1, dest1) <= fix2 <= max(start1, dest1) :
            return True;
        else :
            return False

Graph = [[] for _ in range(K + 2)];
for i in range(1, K + 1) :
    for j in range(i + 1, K + 1) :
        if checkIfCanGo(Info[i], Info[j]) :
            Graph[Info[i][0]].append(Info[j][0]);
            Graph[Info[j][0]].append(Info[i][0]);

for i in range(1, K + 1) :
    num, dirr, fix, start, dest = Info[i];
    if dirr == 0 :
        if sx == fix and min(start, dest) <= sy <= max(start, dest) :
            Graph[0].append(num);
            Graph[num].append(0);
        if dx == fix and min(start, dest) <= dy <= max(start, dest) :
            Graph[K + 1].append(num);
            Graph[num].append(K + 1);
    elif dirr == 1 :
        if sy == fix and min(start, dest) <= sx <= max(start, dest) :
            Graph[0].append(num);
            Graph[num].append(0);
        if dy == fix and min(start, dest) <= dx <= max(start, dest) :
            Graph[K + 1].append(num);
            Graph[num].append(K + 1);

IsVisited = [0] * (K + 2);
q = deque([(0, 0)]);
IsVisited[0] = 1;
Answer = -1;
while q :
    nowDist, nowNode = q.popleft();

    if nowNode == K + 1 :
        Answer = nowDist - 1;
        break;

    for nextNode in Graph[nowNode] :
        if IsVisited[nextNode] == 1 :
            continue;
        nextDist = nowDist + 1;
        q.append((nextDist, nextNode));
        IsVisited[nextNode] = 1;

print(Answer);