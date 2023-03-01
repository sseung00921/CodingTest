import sys;
input = sys.stdin.readline;

s = list(input().rstrip());
up = list(input().rstrip());
down = list(input().rstrip());

d = [[[-1] * (len(s) + 1) for _ in range(2)] for _ in range(len(up) + 1)];

def dfs(col, upDown, cnt) : #0은 위를 밟은 거 1은 아래를 밟은 거
    if cnt == len(s) :
        d[col][upDown][cnt] = 1;
        return d[col][upDown][cnt] ;
    if col == len(up) :
        d[col][upDown][cnt] = 0;
        return d[col][upDown][cnt] ;
    if d[col][upDown][cnt] != -1 :
        return d[col][upDown][cnt];

    charToStepOn = s[cnt];
    summ = 0;
    if upDown == 0 :
        if up[col] == charToStepOn :
            summ += dfs(col + 1, 1, cnt + 1);
    elif upDown == 1 :
        if down[col] == charToStepOn :
            summ += dfs(col + 1, 0, cnt + 1);
    summ += dfs(col + 1, upDown, cnt);

    d[col][upDown][cnt] = summ;
    return d[col][upDown][cnt];

print(dfs(0, 0, 0) + dfs(0, 1, 0));