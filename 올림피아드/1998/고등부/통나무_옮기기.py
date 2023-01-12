import sys;
input = sys.stdin.readline;
dr = [-1,0,1,0];
dc = [0,-1,0,1];
from collections import deque;

def turn(Bpos) :
    a, center, b = Bpos;
    if a[0] == b[0] : #가로
        a = (center[0] - 1, center[1]);
        b = (center[0] + 1, center[1]);
    elif a[1] == b[1] : #세로
        a = (center[0], center[1] - 1);
        b = (center[0], center[1] + 1);

    return (a, center, b);

n = int(input());
Board = [];
for _ in range(n) :
    strr = input().rstrip();
    tmpArr = [];
    for c in strr :
        tmpArr.append(c);
    Board.append(tmpArr)

Bpos = []
Epos = []
for i in range(len(Board)) :
    for j in range(len(Board)) :
        if Board[i][j] == 'B' or Board[i][j] == 'E' :
            if Board[i][j] == 'B' :
                Bpos.append((i, j));
            elif Board[i][j] == 'E' :
                Epos.append((i, j));
            Board[i][j] = '0';

Visited = [[[False] * 2 for _ in range(50)] for _ in range(50)];
q = deque([(Bpos, 0)]);
if Bpos[0][0] == Bpos[2][0] :
    Visited[Bpos[1][0]][Bpos[1][1]][0] = True;
elif Bpos[0][1] == Bpos[2][1] :
    Visited[Bpos[1][0]][Bpos[1][1]][1] = True;
while q :
    Bpos, movedCnt = q.popleft();
    if Epos == Bpos :
        print(movedCnt);
        break;
    isGaro = Bpos[0][0] == Bpos[2][0];
    for dir in range(4) :
        if dir == 0 : #북
            if Bpos[0][0] == 0 :
                continue;
            if Board[Bpos[0][0] - 1][Bpos[0][1]] != '0' or Board[Bpos[1][0] - 1][Bpos[1][1]] != '0' or Board[Bpos[2][0] - 1][Bpos[2][1]] != '0':
                continue;
            if isGaro :
                if Visited[Bpos[1][0] - 1][Bpos[1][1]][0] == True :
                    continue;
            else :
                if Visited[Bpos[1][0] - 1][Bpos[1][1]][1] == True :
                    continue;
            if isGaro :
                Visited[Bpos[1][0] - 1][Bpos[1][1]][0] = True;
            else :
                Visited[Bpos[1][0] - 1][Bpos[1][1]][1] = True;
            q.append(([(Bpos[0][0] - 1, Bpos[0][1]), (Bpos[1][0] - 1, Bpos[1][1]), (Bpos[2][0] - 1, Bpos[2][1])], movedCnt + 1));
        if dir == 1 :#서
            if Bpos[0][1] == 0 :
                continue;
            if Board[Bpos[0][0]][Bpos[0][1] - 1] != '0' or Board[Bpos[1][0]][Bpos[1][1] - 1] != '0' or Board[Bpos[2][0]][Bpos[2][1] - 1] != '0':
                continue;
            if isGaro :
                if Visited[Bpos[1][0]][Bpos[1][1] - 1][0] == True :
                    continue;
            else :
                if Visited[Bpos[1][0]][Bpos[1][1] - 1][1] == True :
                    continue;
            if isGaro :
                Visited[Bpos[1][0]][Bpos[1][1] - 1][0] = True;
            else :
                Visited[Bpos[1][0]][Bpos[1][1] - 1][1] = True;
            q.append(([(Bpos[0][0], Bpos[0][1] - 1), (Bpos[1][0], Bpos[1][1] - 1), (Bpos[2][0], Bpos[2][1] - 1)], movedCnt + 1));
        if dir == 2 : #남
            if Bpos[2][0] == n - 1 :
                continue;
            if Board[Bpos[0][0] + 1][Bpos[0][1]] != '0' or Board[Bpos[1][0] + 1][Bpos[1][1]] != '0' or Board[Bpos[2][0] + 1][Bpos[2][1]] != '0':
                continue;
            if isGaro :
                if Visited[Bpos[1][0] + 1][Bpos[1][1]][0] == True :
                    continue;
            else :
                if Visited[Bpos[1][0] + 1][Bpos[1][1]][1] == True :
                    continue;
            if isGaro :
                Visited[Bpos[1][0] + 1][Bpos[1][1]][0] = True;
            else :
                Visited[Bpos[1][0] + 1][Bpos[1][1]][1] = True;
            q.append(([(Bpos[0][0] + 1, Bpos[0][1]), (Bpos[1][0] + 1, Bpos[1][1]), (Bpos[2][0] + 1, Bpos[2][1])], movedCnt + 1));
        if dir == 3 :#동
            if Bpos[2][1] == n - 1 :
                continue;
            if Board[Bpos[0][0]][Bpos[0][1] + 1] != '0' or Board[Bpos[1][0]][Bpos[1][1] + 1] != '0' or Board[Bpos[2][0]][Bpos[2][1] + 1] != '0':
                continue;
            if isGaro :
                if Visited[Bpos[1][0]][Bpos[1][1] + 1][0] == True :
                    continue;
            else :
                if Visited[Bpos[1][0]][Bpos[1][1] + 1][1] == True :
                    continue;
            if isGaro :
                Visited[Bpos[1][0]][Bpos[1][1] + 1][0] = True;
            else :
                Visited[Bpos[1][0]][Bpos[1][1] + 1][1] = True;
            q.append(([(Bpos[0][0], Bpos[0][1] + 1), (Bpos[1][0], Bpos[1][1] + 1), (Bpos[2][0], Bpos[2][1] + 1)], movedCnt + 1));
    #회전
    centerR, centerC = Bpos[1][0], Bpos[1][1];
    canTurn = True;
    if centerR == 0 or centerR == n - 1 or centerC == 0 or centerC == n - 1 :
        canTurn = False;
    if canTurn :
        for i in range(centerR - 1, centerR + 2) :
            for j in range(centerC - 1, centerC + 2) :
                if Board[i][j] == '1' :
                    canTurn = False;
                    break;
            if not canTurn :
                break;
    if canTurn :
        nBpos = turn(Bpos);
        if isGaro :
            if Visited[nBpos[1][0]][nBpos[1][1]][1] == False :
                Visited[nBpos[1][0]][nBpos[1][1]][1] = True;
                q.append((nBpos, movedCnt + 1));
        else :
            if Visited[nBpos[1][0]][nBpos[1][1]][0] == False :
                Visited[nBpos[1][0]][nBpos[1][1]][0] = True;
                q.append((nBpos, movedCnt + 1));
    if len(q) == 0 :
        print(0);

