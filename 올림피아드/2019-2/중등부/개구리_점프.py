import sys;
input = sys.stdin.readline;
N, Q = map(int, input().split());
Bars = [];
for i in range(1, N + 1) :
    sx, ex, y = map(int, input().split());
    Bars.append((sx, ex, y, i));
Questions = [];
for _ in range(Q) :
    a, b = map(int, input().split())
    Questions.append((a, b));

Parents = [i for i in range(0, N + 1)];
def findParnet(x) :
    if Parents[x] != x :
        Parents[x] = findParnet(Parents[x]);
        return Parents[x];
    return Parents[x];

def unionParent(a, b) :
    a = findParnet(a);
    b = findParnet(b);
    if a < b :
        Parents[b] = a;
    else :
        Parents[a] = b;

Bars.sort();
nowSx, nowEx, nowY, nowNum = Bars[0];
for i in range(1, N) :
    nextSx, nextEx, nextY, nextNum = Bars[i];
    if nextSx <= nowEx :
        unionParent(nowNum, nextNum);
        if nextEx > nowEx :
            nowSx, nowEx, nowY, nowNum = nextSx, nextEx, nextY, nextNum;
    else :
        nowSx, nowEx, nowY, nowNum = nextSx, nextEx, nextY, nextNum;

for question in Questions :
    a, b = question;
    if findParnet(a) == findParnet(b) :
        print(1);
    else :
        print(0);
