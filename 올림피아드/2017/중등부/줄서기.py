import sys;
input = sys.stdin.readline;

N, M = map(int, input().split());
Called = [0] * (N + 1);
SmallCnt = [0] * (N + 1);
for _ in range(M) :
    bigger, smaller = map(int, input().split());
    Called[smaller] += 1;
    SmallCnt[bigger] += 1;

for i in range(1, N + 1) :
    SmallCnt[i] += (i - Called[i]);

IsDuplicated = False;
SetForduplicated = set();
for i in range(1, N + 1) :
    if SmallCnt[i] in SetForduplicated :
        IsDuplicated = True;
        break;
    SetForduplicated.add(SmallCnt[i]);

if IsDuplicated :
    print(-1);
else :
    print(*SmallCnt[1 : ]);