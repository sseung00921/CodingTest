import sys;
input = sys.stdin.readline;
from collections import deque;

A, B, C, D = map(int, input().split());
BoardMap = dict();
BoardMap[(0, 0)] = 0;
q = deque([(0, 0)]);
Answer = -1;
while q :
    x, y = q.popleft();

    if x == C and y == D :
        Answer = BoardMap[(x, y)];
        break;

    if (A, y) not in BoardMap :
        BoardMap[(A, y)] = BoardMap[(x, y)] + 1;
        q.append((A, y));

    if (x, B) not in BoardMap :
        BoardMap[(x, B)] = BoardMap[(x, y)] + 1;
        q.append((x, B));

    if (0, y) not in BoardMap :
        BoardMap[(0, y)] = BoardMap[(x, y)] + 1;
        q.append((0, y));

    if (x, 0) not in BoardMap :
        BoardMap[(x, 0)] = BoardMap[(x, y)] + 1;
        q.append((x, 0));

    if x < B - y :
        if (0, y + x) not in BoardMap :
            BoardMap[(0, y + x)] = BoardMap[(x, y)] + 1;
            q.append((0, y + x));
    else :
        if (x + y - B, B) not in BoardMap :
            BoardMap[(x + y - B, B)] = BoardMap[(x, y)] + 1;
            q.append((x + y - B, B));

    if y < A - x :
        if (x + y, 0) not in BoardMap :
            BoardMap[(x + y, 0)] = BoardMap[(x, y)] + 1;
            q.append((x + y, 0));
    else :
        if (A, y + x - A) not in BoardMap :
            BoardMap[(A, y + x - A)] = BoardMap[(x, y)] + 1;
            q.append((A, y + x - A));

print(Answer);