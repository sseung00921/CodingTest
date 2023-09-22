import sys;

input = sys.stdin.readline;
N = int(input());
K = int(input());
dFull = [0] * 41;
dOneEmpty = [0] * 41;

dFull[0] = 1;
dFull[1] = 1;
dFull[2] = 2;
for i in range(3, 41) :
    dFull[i] = dFull[i - 1] + dFull[i - 2];

dOneEmpty[2] = 2;
for i in range(3, 41) :
    dOneEmpty[i] = dOneEmpty[i - 1] + dFull[i - 1];

Answer = 0;
#빈자리 안 씀
Answer += dFull[K - 1] * dFull[N - K];
#빈자리 씀
for i in range(1, N + 1) :
    if i == K :
        continue;
