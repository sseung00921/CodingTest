import sys;
from bisect import bisect_left;

input = sys.stdin.readline;
N, Q = map(int, input().split());
Cities = [];
CityPoses = [];
for _ in range(N) :
    a, x = map(int, input().split());
    Cities.append((a, x));
    CityPoses.append(x);
Hubos = [];
for _ in range(Q) :
    Hubos.append(int(input()));

Cities.sort(key = lambda x : x[1]);
CityPoses.sort();
CumSumFromLeft = [0] * N;
CumPopFromLeft = [0] * N;
CumPop = 0;
CumSum = 0;
for i in range(1, N) :
    CumPop += Cities[i - 1][0]
    CumSum += CumPop * (Cities[i][1] - Cities[i - 1][1]);
    CumSumFromLeft[i] = CumSum;
    CumPopFromLeft[i] = CumPop;

CumSumFromRight = [0] * N;
CumPopFromRight = [0] * N;
CumPop = 0;
CumSum = 0;
for i in range(N - 2, -1, -1) :
    CumPop += Cities[i + 1][0]
    CumSum += CumPop * (Cities[i + 1][1] - Cities[i][1]);
    CumSumFromRight[i] = CumSum;
    CumPopFromRight[i] = CumPop;

CumPopMost = 0;
for i in range(N) :
    CumPopMost += Cities[i][0];

for hubo in Hubos :
    idx = bisect_left(CityPoses, hubo);
    if idx == 0 :
        print(CumSumFromRight[0] + (CumPopMost * (CityPoses[0] - hubo)));
    elif idx == N :
        print(CumSumFromLeft[-1] + (CumPopMost * (hubo - CityPoses[-1])));
    else :
        print(CumSumFromLeft[idx - 1] + (CumPopFromLeft[idx] * (hubo - CityPoses[idx - 1]))
            + CumSumFromRight[idx] + (CumPopFromRight[idx - 1] * (CityPoses[idx] - hubo)));