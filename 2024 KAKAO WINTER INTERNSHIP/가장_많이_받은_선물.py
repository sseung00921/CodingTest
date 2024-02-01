M = dict()
Graph = None
N = 0;
def solution(friends, gifts):
    global N;
    global Graph;
    N = len(friends);
    Graph = [[0] * N for _ in range(N)];
    TotalGive = [0] * N;
    TotalGot = [0] * N;
    Points = [0] * N;
    num = 0;
    for f in friends :
        M[f] = num;
        num += 1;
    for g in gifts :
        sender, reciever = g.split();
        sender = M[sender];
        reciever = M[reciever];
        Graph[sender][reciever] += 1;
        TotalGive[sender] += 1;
        TotalGot[reciever] += 1;
    for i in range(N) :
        Points[i] = TotalGive[i] - TotalGot[i];
    AnswerArr = [0] * N;
    for i in range(N) :
        for j in range(i + 1, N) :
            if Graph[i][j] > Graph[j][i] :
                AnswerArr[i] += 1;
            elif Graph[i][j] < Graph[j][i] :
                AnswerArr[j] += 1;
            elif Graph[i][j] == Graph[j][i] :
                if Points[i] > Points[j] :
                    AnswerArr[i] += 1;
                elif Points[i] < Points[j] :
                    AnswerArr[j] += 1;

    answer = max(AnswerArr);
    return answer

friends = ["muzi", "ryan", "frodo", "neo"];
gifts = ["muzi frodo", "muzi frodo", "ryan muzi", "ryan muzi", "ryan muzi", "frodo muzi", "frodo ryan", "neo muzi"];
print(solution(friends, gifts));