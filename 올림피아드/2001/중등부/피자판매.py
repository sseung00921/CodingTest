import sys;
input = sys.stdin.readline;

reqSize = int(input());
aSize, bSize = map(int, input().split());
aSlices = [];
bSlices = [];
for _ in range(aSize) :
    aSlices.append(int(input()));
for _ in range(bSize) :
    bSlices.append(int(input()));
aSlices += aSlices[ : -1];
bSlices += bSlices[ : -1];

aP = [[0] * (aSize + 1) for _ in range(aSize)];
bP = [[0] * (bSize + 1) for _ in range(bSize)];
aD = [0] * 1000001;
bD = [0] * 1000001;

for i in range(aSize) :
    aP[i][1] = aSlices[i];
    aD[aP[i][1]] += 1;
for i in range(bSize) :
    bP[i][1] = bSlices[i];
    bD[bP[i][1]] += 1;

for i in range(2, aSize) :
    for j in range(0, aSize) :
        aP[j][i] = aP[j][i - 1] + aSlices[j + i - 1];
        aD[aP[j][i]] += 1;

for i in range(2, bSize) :
    for j in range(0, bSize) :
        bP[j][i] = bP[j][i - 1] + bSlices[j + i - 1];
        bD[bP[j][i]] += 1;

aD[sum(aSlices[ :  aSize])] += 1;
bD[sum(bSlices[ :  bSize])] += 1;

answer = 0;
for i in range(1, reqSize + 1) :
    answer += aD[i]*bD[reqSize - i];
answer += aD[reqSize];
answer += bD[reqSize];
print(answer)