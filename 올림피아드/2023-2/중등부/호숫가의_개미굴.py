import sys;

input = sys.stdin.readline;
from collections import deque;

N = int(input());
d = [0] * (N + 1);
d[1] = 1;
d[2] = 1;
for i in range(3, N + 1):
    d[i] = max(d[i - 2] + 1, d[i - 1]);
Arr = list(map(int, input().split()));

if Arr.count(0) == N:
    if N <= 3:
        print(1);
    else:
        Answer = max(d[N - 3] + 1, d[N - 1]);
        print(Answer);
else:
    SplitIdx = -1;
    for i in range(N):
        if Arr[i] != 0:
            SplitIdx = i;
            break;

    Arr = Arr[SplitIdx:] + Arr[: SplitIdx];

    Answer = 0;
    ContinueCnt = 0;
    for i in range(N):
        if Arr[i] > 0:
            Answer += Arr[i];
            Answer += d[ContinueCnt];
            ContinueCnt = 0;
        else:
            ContinueCnt += 1;
    Answer += d[ContinueCnt];

    print(Answer);