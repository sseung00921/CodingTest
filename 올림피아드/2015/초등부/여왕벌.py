import sys;
input = sys.stdin.readline;
from collections import deque;

M, N = map(int, input().split());
Board = [[1] * M for _ in range(M)];
EdgeGrowingPlan = [0] * (2*M - 1);
for _ in range(N) :
    a, b, c = map(int, input().split());
    if b == 0 and c == 0 :
        continue;
    elif b != 0 and c == 0 :
        EdgeGrowingPlan[a] += 1;
    elif b == 0 and c != 0 :
        EdgeGrowingPlan[a] += 2;
    else :
        EdgeGrowingPlan[a] += 1;
        EdgeGrowingPlan[a + b] += 1;

for i in range(1, len(EdgeGrowingPlan)) :
    EdgeGrowingPlan[i] += EdgeGrowingPlan[i - 1];

EdgeGrowingPlan = deque(EdgeGrowingPlan);
for i in range(M - 1, -1, -1) :
    Board[i][0] += EdgeGrowingPlan.popleft();
for i in range(1, M) :
    Board[0][i] += EdgeGrowingPlan.popleft();

for j in range(1, M) :
    for i in range(1, M) :
        Board[i][j] += Board[i - 1][j] - 1;

for e in Board :
    print(*e);