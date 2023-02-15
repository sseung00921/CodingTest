import sys;
input = sys.stdin.readline;

Board = [];
for _ in range(19) :
    Board.append(list(map(int, input().split())));

winBlocks = [];

def checkIfWin(r, c, who) :
    #시계방향으로 돌자 우선 위.
    for i in range(6) :
        nr = r - i;
        nc = c;
        pr = r + 1;
        pc = c;
        if i <= 4 and (nr < 0 or nr >= 19 or nc < 0 or nc >= 19) :
            winBlocks.clear();
            break;
        if i <= 4 and Board[nr][nc] != who :
            winBlocks.clear();
            break;
        if i == 5 :
            if nr < 0 or nr >= 19 or nc < 0 or nc >= 19 :
                if (0 <= pr < 19 and 0 <= pc < 19) and Board[pr][pc] == who :
                    winBlocks.clear();
                    break;
                return True;
            if Board[nr][nc] == who :
                winBlocks.clear();
                break;
            if Board[nr][nc] != who :
                if (0 <= pr < 19 and 0 <= pc < 19) and Board[pr][pc] == who :
                    winBlocks.clear();
                    break;
                return True;
        winBlocks.append((nr, nc));
    #1시방향
    for i in range(6) :
        nr = r - i;
        nc = c + i;
        pr = r + 1;
        pc = c - 1;
        if i <= 4 and (nr < 0 or nr >= 19 or nc < 0 or nc >= 19) :
            winBlocks.clear();
            break;
        if i <= 4 and Board[nr][nc] != who :
            winBlocks.clear();
            break;
        if i == 5 :
            if nr < 0 or nr >= 19 or nc < 0 or nc >= 19 :
                if (0 <= pr < 19 and 0 <= pc < 19) and Board[pr][pc] == who :
                    winBlocks.clear();
                    break;
                return True;
            if Board[nr][nc] == who :
                winBlocks.clear();
                break;
            if Board[nr][nc] != who :
                if (0 <= pr < 19 and 0 <= pc < 19) and Board[pr][pc] == who :
                    winBlocks.clear();
                    break;
                return True;
        winBlocks.append((nr, nc));
    #오른쪽
    for i in range(6) :
        nr = r;
        nc = c + i;
        pr = r;
        pc = c - 1;
        if i <= 4 and (nr < 0 or nr >= 19 or nc < 0 or nc >= 19) :
            winBlocks.clear();
            break;
        if i <= 4 and Board[nr][nc] != who :
            winBlocks.clear();
            break;
        if i == 5 :
            if nr < 0 or nr >= 19 or nc < 0 or nc >= 19 :
                if (0 <= pr < 19 and 0 <= pc < 19) and Board[pr][pc] == who :
                    winBlocks.clear();
                    break;
                return True;
            if Board[nr][nc] == who :
                winBlocks.clear();
                break;
            if Board[nr][nc] != who :
                if (0 <= pr < 19 and 0 <= pc < 19) and Board[pr][pc] == who :
                    winBlocks.clear();
                    break;
                return True;
        winBlocks.append((nr, nc));
    #5시 방향
    for i in range(6) :
        nr = r + i;
        nc = c + i;
        pr = r - 1;
        pc = c - 1;
        if i <= 4 and (nr < 0 or nr >= 19 or nc < 0 or nc >= 19) :
            winBlocks.clear();
            break;
        if i <= 4 and Board[nr][nc] != who :
            winBlocks.clear();
            break;
        if i == 5 :
            if nr < 0 or nr >= 19 or nc < 0 or nc >= 19 :
                if (0 <= pr < 19 and 0 <= pc < 19) and Board[pr][pc] == who :
                    winBlocks.clear();
                    break;
                return True;
            if Board[nr][nc] == who :
                winBlocks.clear();
                break;
            if Board[nr][nc] != who :
                if (0 <= pr < 19 and 0 <= pc < 19) and Board[pr][pc] == who :
                    winBlocks.clear();
                    break;
                return True;
        winBlocks.append((nr, nc));
    #아래쪽
    for i in range(6) :
        nr = r + i;
        nc = c;
        pr = r - 1;
        pc = c;
        if i <= 4 and (nr < 0 or nr >= 19 or nc < 0 or nc >= 19) :
            winBlocks.clear();
            break;
        if i <= 4 and Board[nr][nc] != who :
            winBlocks.clear();
            break;
        if i == 5 :
            if nr < 0 or nr >= 19 or nc < 0 or nc >= 19 :
                if (0 <= pr < 19 and 0 <= pc < 19) and Board[pr][pc] == who :
                    winBlocks.clear();
                    break;
                return True;
            if Board[nr][nc] == who :
                winBlocks.clear();
                break;
            if Board[nr][nc] != who :
                if (0 <= pr < 19 and 0 <= pc < 19) and Board[pr][pc] == who :
                    winBlocks.clear();
                    break;
                return True;
        winBlocks.append((nr, nc));
    #7시 방향
    for i in range(6) :
        nr = r + i;
        nc = c - i;
        pr = r - 1;
        pc = c + 1;
        if i <= 4 and (nr < 0 or nr >= 19 or nc < 0 or nc >= 19) :
            winBlocks.clear();
            break;
        if i <= 4 and Board[nr][nc] != who :
            winBlocks.clear();
            break;
        if i == 5 :
            if nr < 0 or nr >= 19 or nc < 0 or nc >= 19 :
                if (0 <= pr < 19 and 0 <= pc < 19) and Board[pr][pc] == who :
                    winBlocks.clear();
                    break;
                return True;
            if Board[nr][nc] == who :
                winBlocks.clear();
                break;
            if Board[nr][nc] != who :
                if (0 <= pr < 19 and 0 <= pc < 19) and Board[pr][pc] == who :
                    winBlocks.clear();
                    break;
                return True;
        winBlocks.append((nr, nc));
    #왼쪽
    for i in range(6) :
        nr = r;
        nc = c - i;
        pr = r;
        pc = c + 1;
        if i <= 4 and (nr < 0 or nr >= 19 or nc < 0 or nc >= 19) :
            winBlocks.clear();
            break;
        if i <= 4 and Board[nr][nc] != who :
            winBlocks.clear();
            break;
        if i == 5 :
            if nr < 0 or nr >= 19 or nc < 0 or nc >= 19 :
                if (0 <= pr < 19 and 0 <= pc < 19) and Board[pr][pc] == who :
                    winBlocks.clear();
                    break;
                return True;
            if Board[nr][nc] == who :
                winBlocks.clear();
                break;
            if Board[nr][nc] != who :
                if (0 <= pr < 19 and 0 <= pc < 19) and Board[pr][pc] == who :
                    winBlocks.clear();
                    break;
                return True;
        winBlocks.append((nr, nc));
    #11시 방향
    for i in range(6) :
        nr = r - i;
        nc = c - i;
        pr = r + 1;
        pc = c + 1;
        if i <= 4 and (nr < 0 or nr >= 19 or nc < 0 or nc >= 19) :
            winBlocks.clear();
            break;
        if i <= 4 and Board[nr][nc] != who :
            winBlocks.clear();
            break;
        if i == 5 :
            if nr < 0 or nr >= 19 or nc < 0 or nc >= 19 :
                if (0 <= pr < 19 and 0 <= pc < 19) and Board[pr][pc] == who :
                    winBlocks.clear();
                    break;
                return True;
            if Board[nr][nc] == who :
                winBlocks.clear();
                break;
            if Board[nr][nc] != who :
                if (0 <= pr < 19 and 0 <= pc < 19) and Board[pr][pc] == who :
                    winBlocks.clear();
                    break;
                return True;
        winBlocks.append((nr, nc));
    return False;

getWin = False;
for i in range(19) :
    for j in range(19) :
        if Board[i][j] == 0 :
            continue;
        if checkIfWin(i, j, Board[i][j]) :
            getWin = True;
            print(Board[i][j]);
            winBlocks.sort(key = lambda x : (x[1], x[0]));
            print(winBlocks[0][0] + 1, winBlocks[0][1] + 1);
            break;
    if getWin :
        break;

if not getWin :
    print(0);
"""
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
"""