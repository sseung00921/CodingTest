from collections import deque;

dr = [-1,0,1,0];
dc = [0,-1,0,1];

Mapper = dict()
Land = None;
N = 0;
M = 0;
Cnt = 2;

def oob(r, c) :
    if r < 0 or r >= N or c < 0 or c >= M :
        return True;
    return False;

def bfs() :
    global Cnt;
    for i in range(N) :
        for j in range(M) :
            if Land[i][j] != 1 :
                continue;
            q = deque([(i, j)]);
            Land[i][j] = Cnt;
            while q :
                r, c = q.popleft();
                for dir in range(4) :
                    nr = r + dr[dir];
                    nc = c + dc[dir];
                    if oob(nr, nc) :
                        continue;
                    if Land[nr][nc] != 1 :
                        continue;
                    Land[nr][nc] = Cnt;
                    q.append((nr, nc));
            Cnt += 1;

def setMapper() :
    for i in range(N) :
        for j in range(M) :
            if Land[i][j] > 1 :
                if Land[i][j] not in Mapper :
                    Mapper[Land[i][j]] = 1;
                else :
                    Mapper[Land[i][j]] += 1;

def prettyPrint() :
    for e in Land :
        print(*e);

def solution(land):
    global Land; global N; global M;
    Land = land; N = len(Land); M = len(Land[0]);

    bfs();
    setMapper();

    answer = 0
    for j in range(M) :
        sett = set()
        for i in range(N) :
            if Land[i][j] > 1 :
                sett.add(Land[i][j]);
        tmp = 0;
        for e in sett :
            tmp += Mapper[e];
        answer = max(answer, tmp);
    return answer

land = [[1, 0, 1, 0, 1, 1], [1, 0, 1, 0, 0, 0], [1, 0, 1, 0, 0, 1], [1, 0, 0, 1, 0, 0], [1, 0, 0, 1, 0, 1], [1, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1]];
print(solution(land));