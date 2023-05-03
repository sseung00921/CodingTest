import sys;
sys.setrecursionlimit(10**6);

N = 0;
M = 0;
R = 0;
C = 0;
K = 0;
Answer = None;

def calDist(r, c) :
    return abs(R - r) + abs(C - c);

def notOobChecker(r, c) :
    if r <= 0 or r > N or c <= 0 or c > M :
        return False;
    return True;

def dfs(nowR, nowC, nowK, nowTxt) :
    global Answer;

    if Answer != None :
        return;

    if calDist(nowR, nowC) > K - nowK :
        return;

    if nowK == K :
        if nowR == R and nowC == C :
            Answer = nowTxt;
        return;

    if notOobChecker(nowR + 1, nowC) :
        dfs(nowR + 1, nowC, nowK + 1, nowTxt + 'd');
    if notOobChecker(nowR, nowC - 1) :
        dfs(nowR, nowC - 1, nowK + 1, nowTxt + 'l');
    if notOobChecker(nowR, nowC + 1) :
        dfs(nowR, nowC + 1, nowK + 1, nowTxt + 'r');
    if notOobChecker(nowR - 1, nowC) :
        dfs(nowR - 1, nowC, nowK + 1, nowTxt + 'u');

def solution(n, m, x, y, r, c, k):
    global N;
    global M;
    global R;
    global C;
    global K;
    global Answer;
    N = n;
    M = m;
    R = r;
    C = c;
    K = k;

    if (K - calDist(x, y)) % 2 == 1 :
        return "impossible";

    dfs(x, y, 0, '');
    if Answer == None :
        Answer = "impossible";
    return Answer;

n = 3;
m = 4;
x = 2;
y = 3;
r = 3;
c = 1;
k = 5;
print(solution(n, m, x, y, r, c, k));