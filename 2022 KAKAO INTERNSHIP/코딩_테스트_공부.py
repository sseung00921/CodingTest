def solution(alp, cop, problems):
    for p in problems :
        p[0] -= alp;
        if p[0] < 0 :
            p[0] = 0;
        p[1] -= cop;
        if p[1] < 0 :
            p[1] = 0;
    MaxAlp = -1;
    MaxCop = -1;
    for p in problems :
        MaxAlp = max(MaxAlp, p[0]);
        MaxCop = max(MaxCop, p[1]);

    INF = int(1e10);
    d = [[INF] * (MaxCop + 1) for _ in range(MaxAlp + 1)];
    d[0][0] = 0;
    for i in range(0, MaxAlp + 1) :
        for j in range(0, MaxCop + 1) :
            if j < MaxCop :
                d[i][j + 1] = min(d[i][j + 1], d[i][j] + 1);
            if i < MaxAlp :
                d[i + 1][j] = min(d[i + 1][j], d[i][j] + 1);
            for p in problems :
                alpReq, copReq, alpRwd, copRwd, cost = p;
                if i >= alpReq and j >= copReq :
                    nextAlp = min(i + alpRwd, MaxAlp);
                    nextCop = min(j + copRwd, MaxCop);
                    d[nextAlp][nextCop] = min(d[nextAlp][nextCop], d[i][j] + cost);

    return d[MaxAlp][MaxCop];

alp = 0;
cop = 0;
problems = [[0,0,2,1,2],[4,5,3,1,2],[4,11,4,0,2],[10,4,0,4,2]];
print(solution(alp, cop, problems));
