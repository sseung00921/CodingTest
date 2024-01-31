import sys;
input = sys.stdin.readline;
from bisect import bisect_right, bisect_left;

N, Q = map(int, input().split());
GraphForVertical = [[] for _ in range(200002)];
GraphForHorizontal = [[] for _ in range(200002)];
for _ in range(N) :
    x, y, w = map(int, input().split());
    GraphForVertical[x].append([y, w]);
    GraphForHorizontal[y].append([x, w]);

for i in range(200002) :
    GraphForVertical[i].sort();
    GraphForHorizontal[i].sort();

VerticalIdxInfo = [[-1] for _ in range(200002)];
VerticalSumInfo = [[0] for _ in range(200002)];
HorizontalIdxInfo = [[-1] for _ in range(200002)];
HorizontalSumInfo = [[0] for _ in range(200002)];
for i in range(200002) :
    for j in range(0, len(GraphForVertical[i])) :
        VerticalIdxInfo[i].append(GraphForVertical[i][j][0]);
        VerticalSumInfo[i].append(GraphForVertical[i][j][1]);
    for j in range(0, len(GraphForHorizontal[i])) :
        HorizontalIdxInfo[i].append(GraphForHorizontal[i][j][0]);
        HorizontalSumInfo[i].append(GraphForHorizontal[i][j][1]);

for i in range(200002) :
    for j in range(1, len(VerticalSumInfo[i])) :
        VerticalSumInfo[i][j] += VerticalSumInfo[i][j - 1];
    for j in range(1, len(HorizontalSumInfo[i])) :
        HorizontalSumInfo[i][j] += HorizontalSumInfo[i][j - 1];

Answer = 0;
nowX = 1; nowY = 1;
for _ in range(Q) :
    d, v = map(int, input().split());
    if d == 0 :
        nextX = nowX + v;
        startIdx = bisect_right(HorizontalIdxInfo[nowY], nowX);
        endIdx = bisect_right(HorizontalIdxInfo[nowY], nextX);
        Answer += HorizontalSumInfo[nowY][endIdx - 1] - HorizontalSumInfo[nowY][startIdx - 1];
        nowX = nextX;
    elif d == 1 :
        nextY = nowY + v;
        startIdx = bisect_right(VerticalIdxInfo[nowX], nowY);
        endIdx = bisect_right(VerticalIdxInfo[nowX], nextY);
        Answer += VerticalSumInfo[nowX][endIdx - 1] - VerticalSumInfo[nowX][startIdx - 1];
        nowY = nextY;
    elif d == 2 :
        nextX = nowX - v;
        startIdx = bisect_left(HorizontalIdxInfo[nowY], nextX);
        endIdx = bisect_left(HorizontalIdxInfo[nowY], nowX);
        Answer += HorizontalSumInfo[nowY][endIdx - 1] - HorizontalSumInfo[nowY][startIdx - 1];
        nowX = nextX;
    elif d == 3 :
        nextY = nowY - v;
        startIdx = bisect_left(VerticalIdxInfo[nowX], nextY);
        endIdx = bisect_left(VerticalIdxInfo[nowX], nowY);
        Answer += VerticalSumInfo[nowX][endIdx - 1] - VerticalSumInfo[nowX][startIdx - 1];
        nowY = nextY;

print(Answer);