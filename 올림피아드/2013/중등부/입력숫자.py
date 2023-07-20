import sys;
input = sys.stdin.readline;

N = int(input());
Y = list(map(int, input().split()));
X = [0] * N;

Frm = 0;
for e in Y :
    while X[Frm] != 0 :
        Frm = (Frm + 1) % N;
    X[Frm] = e;
    Frm = (Frm + e) % N;

print(N);
print(*X);