from collections import deque;
dr = [-1, 0, 1, 0];
dc = [0, 1, 0, -1];

def check(place) :
    persons = [];
    for i in range(5) :
        for j in range(5) :
            if place[i][j] == 'P' :
                persons.append((i, j));

    for person in persons :
        sr, sc = person;
        distTable = [[int(1e9)] * 5 for _ in range(5)];
        q = deque([(sr, sc, 0)]);
        distTable[sr][sc] = 0;
        while q :
            r, c, cost = q.popleft();
            for dir in range(4) :
                nr = r + dr[dir];
                nc = c + dc[dir];
                if nr < 0 or nr >= 5 or nc < 0 or nc >= 5 :
                    continue;
                if place[nr][nc] == 'X' :
                    continue;
                nCost = cost + 1;
                if nCost < distTable[nr][nc] :
                    q.append((nr, nc, nCost));
                    distTable[nr][nc] = nCost;

        for i in range(5) :
            for j in range(5) :
                if distTable[i][j] == 0 :
                    continue;
                if place[i][j] == 'P' and distTable[i][j] <= 2 :
                    return False;
    return True;


def solution(places):
    answer = []
    for place in places :
        if check(place) == True :
            answer.append(1);
        else :
            answer.append(0);
    return answer

places = [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]];
print(solution(places));