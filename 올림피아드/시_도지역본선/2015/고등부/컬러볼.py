import sys;
input = sys.stdin.readline;
from bisect import bisect_left;

N = int(input());

SizeForEachColors = [[0] for _ in range(N + 1)];
SizeForAll = [0];
Data = [];
for _ in range(N) :
    color, size = map(int, input().split());
    SizeForEachColors[color].append(size);
    SizeForAll.append(size);
    Data.append((color, size));

for i in range(N + 1) :
    SizeForEachColors[i].sort();
SizeForAll.sort();

SizeSumForEachColors = [[0] for _ in range(N + 1)];
SizeSumForAll = [0];
for i in range(1, N + 1) :
    for j in range(1, len(SizeForEachColors[i])) :
        SizeSumForEachColors[i].append(SizeSumForEachColors[i][-1] + SizeForEachColors[i][j]);

for i in range(1, N + 1) :
    SizeSumForAll.append(SizeSumForAll[-1] + SizeForAll[i]);

for e in Data :
    color, size = e;
    idxInTotal = bisect_left(SizeForAll, size);
    sumInTotal = SizeSumForAll[idxInTotal];
    idxInTheColor = bisect_left(SizeForEachColors[color], size);
    sumInTheColor = SizeSumForEachColors[color][idxInTheColor];
    print(sumInTotal - sumInTheColor);
