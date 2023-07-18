import sys;
input = sys.stdin.readline;
from bisect import bisect_left;

N, S = map(int, input().split());
Info = [(-1, -1)];
PrevIfInstalled = [0] * (N + 1);
for _ in range(N) :
    height, cost = map(int, input().split());
    Info.append((height, cost));

Info.sort();
for i in range(1, N + 1) :
    maxPrevHeightToSeeThis = Info[i][0] - S;
    prevIdx = bisect_left(Info, (maxPrevHeightToSeeThis, 1001)) - 1;
    PrevIfInstalled[i] = prevIdx;

d = [0] * (N + 1);
for i in range(1, N + 1) :
    notInstall = d[i - 1];
    install = d[PrevIfInstalled[i]] + Info[i][1];
    d[i] = max(notInstall, install);

print(d[N]);