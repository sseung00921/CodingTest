dr = [-1,0,1,0];
dc = [0,-1,0,1];
Maze = None;
N = 0;
M = 0;
Answer = int(1e9);
def oob(r, c) :
    if r < 0 or r >= N or c < 0 or c >= M :
        return True;
    return False;

def checkIfVisit(r, c, visitBit) :
    toCheck = r*N + c;
    if (visitBit & (1 << toCheck)) > 0 :
        return True;
    return False;

def setVisitBit(r, c, visitBit) :
    posNum = r*N + c;
    rtnVisitBit = visitBit | (1 << posNum);
    return rtnVisitBit;

def dfs(ar, ac, br, bc, aVisitBit, bVisitBit, cnt) :
    global Answer;
    if Maze[ar][ac] == 3 and Maze[br][bc] == 4 :
        Answer = min(Answer, cnt);
        return;
    elif Maze[ar][ac] != 3 and Maze[br][bc] == 4 :
        for dir in range(4) :
            nar = ar + dr[dir];
            nac = ac + dc[dir];
            if oob(nar, nac) :
                continue;
            if nar == br and nac == bc :
                continue;
            if Maze[nar][nac] == 5 :
                continue;
            if checkIfVisit(nar, nac, aVisitBit) :
                continue;
            nextAVisitBit = setVisitBit(nar, nac, aVisitBit);
            dfs(nar, nac, br, bc, nextAVisitBit, bVisitBit, cnt + 1);
    elif Maze[ar][ac] == 3 and Maze[br][bc] != 4 :
        for dir in range(4) :
            nbr = br + dr[dir];
            nbc = bc + dc[dir];
            if oob(nbr, nbc) :
                continue;
            if nbr == ar and nbc == ac :
                continue;
            if Maze[nbr][nbc] == 5 :
                continue;
            if checkIfVisit(nbr, nbc, bVisitBit) :
                continue;
            nextBVisitBit = setVisitBit(nbr, nbc, bVisitBit);
            dfs(ar, ac, nbr, nbc, aVisitBit, nextBVisitBit, cnt + 1);
    else :
        for adir in range(4) :
            for bdir in range(4) :
                nar = ar + dr[adir];
                nac = ac + dc[adir];
                nbr = br + dr[bdir];
                nbc = bc + dc[bdir];
                if oob(nar, nac) or oob(nbr, nbc) :
                    continue;
                if nar == nbr and nac == nbc or (nar == br and nac == bc and nbr == ar and nbc == ac) :
                    continue;
                if Maze[nar][nac] == 5 or Maze[nbr][nbc] == 5 :
                    continue;
                if checkIfVisit(nar, nac, aVisitBit) or checkIfVisit(nbr, nbc, bVisitBit) :
                    continue;
                nextAVisitBit = setVisitBit(nar, nac, aVisitBit);
                nextBVisitBit = setVisitBit(nbr, nbc, bVisitBit);
                dfs(nar, nac, nbr, nbc, nextAVisitBit, nextBVisitBit, cnt + 1);
    return;

def solution(maze):
    global Maze; global N; global M;
    Maze = maze;
    N = len(Maze);
    M = len(Maze[0]);
    startAr = -1; startAc = -1; startAVisit = 0;
    startBr = -1; startBc = -1; startBVisit = 0;
    for i in range(N) :
        for j in range(M) :
            if Maze[i][j] == 1 :
                startAr = i; startAc = j;
                startAVisit = setVisitBit(i, j, startAVisit);
            if Maze[i][j] == 2 :
                startBr = i; startBc = j;
                startBVisit = setVisitBit(i, j, startBVisit);

    dfs(startAr, startAc, startBr, startBc, startAVisit, startBVisit, 0);

    if Answer == int(1e9) :
        return 0;

    return Answer;

maze = [[4, 1, 2, 3]];
print(solution(maze))