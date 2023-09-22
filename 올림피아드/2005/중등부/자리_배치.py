import sys;

input = sys.stdin.readline;
dFull = [0] * 41;
dOneEmpty = [0] * 41;

dFull[1] = 1;
dFull[2] = 2;
for i in range(3, 41) :
    dFull[i] = dFull[i - 1] + dFull[i - 2];

dOneEmpty[2] = 2;
for i in range(3, 41) :
    dOneEmpty[i] = dOneEmpty[i - 1] + dFull[i - 1];