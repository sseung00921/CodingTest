import sys;
input = sys.stdin.readline;

N, I, M = map(int, input().split());
HI = I // 2;
dx = [1, 0, -1, 0];
dy = [0, 1, 0, -1];
Info = [];
for _ in range(M) :
    x, y = map(int, input().split());
    Info.append((x - 1, y - 1));

def check(sx, sy, l1, l2) :
    d = 0;
    l1Cnt = l1; l2Cnt = l2;
    while d != 4 :
        if d in [0, 2] :
            sx += dx[d];
            l1Cnt -= 1;
            if l1Cnt == 0 :
                l1Cnt = l1;
                d += 1;
        elif d in [1, 3] :
            sy += dy[d];
            l2Cnt -= 1;
            if l2Cnt == 0 :
                l2Cnt = l2;
                d += 1;
        ex = sx + l1;
        ey = sy + l2;
        if sx < 0 or ex >= N or sy < 0 or ey >= N :
            continue;
        calCnt(sx, sy, ex, ey);

def calCnt(sx, sy, ex, ey) :
    global Answer;
    cnt = 0;
    for e in Info :
        x, y = e;
        if sx <= x <= ex and sy <= y <= ey :
            cnt += 1;
    Answer = max(Answer, cnt);
    return cnt;

Answer = 1;
for e in Info :
    ex, ey = e;
    for l1 in range(1, HI) :
        l2 = HI - l1;
        sx = ex - l1;
        sy = ey - l2;
        check(sx, sy, l1, l2);
print(Answer);


