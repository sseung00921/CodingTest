import sys;
input = sys.stdin.readline;
from bisect import bisect_left, bisect_right;

N = int(input());
XIdxes = [];
XVals = [];
for _ in range(N) :
    idx, val = map(int, input().split());
    XIdxes.append(idx);
    XVals.append(val);
M = int(input());
YIdxes = [];
YVals = [];
for _ in range(M) :
    idx, val = map(int, input().split());
    YIdxes.append(idx);
    YVals.append(val);
YSumm = [0] * (M + 1);
YSumm[0] = 0;
for i in range(0, M) :
    YSumm[i + 1] = YSumm[i] + YVals[i];

a = int(input());
b = int(input());
Answer = 0;
for i in range(0, N) :
    left = bisect_left(YIdxes, XIdxes[i] + a);
    right = bisect_right(YIdxes, XIdxes[i] + b);
    Answer += XVals[i]*(YSumm[right] - YSumm[left]);
print(Answer);