import sys;
input = sys.stdin.readline;

n = int(input());
data = [];
for _ in range(n) :
    leftPos, height = map(int, input().split());
    data.append((leftPos, height));

data.sort(key = lambda x : (-x[1], x[0]));

topHeight = data[0][1];
mostRight = data[0][0] + 1;
for i in range(n) :
    if data[i][1] < topHeight :
        break;
    if data[i][0] + 1 > mostRight :
        mostRight = data[i][0] + 1;

checkPoints = [];
checkPoints.append(data[0]);
checkPoints.append((mostRight, topHeight));

criLeftPos = data[0][0];

data.sort(key = lambda x : x[0]);

criLeftIdx = -1;
for i in range(n) :
    if data[i][0] == criLeftPos :
        criLeftIdx = i;
        break;

criRightIdx = -1;
for i in range(n) :
    if (data[i][0] + 1) == mostRight :
        criRightIdx = i;
        break;

startHeight = -1;
for i in range(criLeftIdx) :
    if data[i][1] > startHeight :
        startHeight = data[i][1];
        checkPoints.append(data[i]);

startHeight = -1;
for i in range(n - 1, criRightIdx, -1) :
    if data[i][1] > startHeight :
        startHeight = data[i][1];
        checkPoints.append((data[i][0] + 1, data[i][1]));

checkPoints.sort();
criLeftIdx = -1;
criRightIdx = -1;
for i in range(len(checkPoints)) :
    if checkPoints[i][1] == topHeight and criLeftIdx == -1 :
        criLeftIdx = i;
    if checkPoints[i][1] == topHeight and criLeftIdx != -1 and criRightIdx < checkPoints[i][0] :
        criRightIdx = i;

answer = 0;
for i in range(1, criLeftIdx + 1) :
    width = checkPoints[i][0] - checkPoints[i - 1][0];
    height = checkPoints[i - 1][1];
    answer += (width * height);

answer += ((checkPoints[criRightIdx][0] - checkPoints[criLeftIdx][0]) * topHeight);

for i in range(len(checkPoints) - 2, criRightIdx - 1, -1) :
    width = checkPoints[i + 1][0] - checkPoints[i][0];
    height = checkPoints[i + 1][1];
    answer += (width * height);

print(answer)