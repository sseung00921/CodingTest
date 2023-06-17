import sys;
input = sys.stdin.readline;
from collections import deque;

N = int(input());
Flowers = [];
for _ in range(N) :
    sm, sd, em, ed = map(int, input().split());
    Flowers.append((sm*100 + sd, em * 100 + ed));

Flowers.sort(key = lambda x : (x[0], x[1]));
Flowers = deque(Flowers);
Covered = 301;
NeededFlowerCnt = 0;
while True :
    if Covered >= 1201 :
        break;
    if len(Flowers) == 0 or Covered < Flowers[0][0] :
        break;

    NextCovered = Covered;
    while Flowers :
        startDate, endDate = Flowers[0][0], Flowers[0][1];
        if Covered < startDate :
            break;
        NextCovered = max(NextCovered, endDate);
        Flowers.popleft();

    NeededFlowerCnt += 1;
    Covered = NextCovered;

if Covered >= 1201 :
    print(NeededFlowerCnt);
else :
    print(0);

