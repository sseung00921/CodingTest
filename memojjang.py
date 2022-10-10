import sys;
input = sys.stdin.readline;

n, m = map(int, input().split());
A = [];
for _ in range(n) :
    A.append(list(map(int, input().split())));
m, k = map(int, input().split());
B = [];
for _ in range(m) :
    B.append(list(map(int, input().split())));

AB = [[0] * k for _ in range(n)];

for i in range(n) :
    for j in range(k) :
        e = 0;
        for l in range(m) :
            e += A[i][l]*B[l][j];
        AB[i][j] = e;

for i in range(len(AB)) :
    print(*AB[i]);
