import sys;
sys.setrecursionlimit(10**6);
#0 미정 1 막대 2 도넛 3 팔자 4 무관정점
Graph = [[] for _ in range(1000002)];
Indegree = [0] * 1000002;
IsVisitedAndStatus = [0] * 1000002;
AnswerArr = [0] * 4;
ExistSet = set();
def goThroughAndCheck(nowNode, numToWrite) :
    IsVisitedAndStatus[nowNode] = numToWrite;
    for nextNode in Graph[nowNode] :
        if IsVisitedAndStatus[nextNode] != 0 :
            continue;
        goThroughAndCheck(nextNode, numToWrite);

def solution(edges):
    for e in edges :
        a, b = e;
        Graph[a].append(b);
        Indegree[b] += 1;
        ExistSet.add(a);
        ExistSet.add(b);
    for i in range(1, 1000002) :
        if i not in ExistSet :
            continue;
        if len(Graph[i]) >= 2 :
            if Indegree[i] == 0 :
                IsVisitedAndStatus[i] = 4;
                AnswerArr[0] = i;
                for nextNode in Graph[i] :
                    Indegree[nextNode] -= 1;
            elif Indegree[i] > 0 :
                if IsVisitedAndStatus[i] == 0 :
                    goThroughAndCheck(i, 3);
                    AnswerArr[3] += 1;
    for i in range(1, 1000002) :
        if i not in ExistSet :
            continue;
        if IsVisitedAndStatus[i] == 0 and Indegree[i] == 0 :
            goThroughAndCheck(i, 1);
            AnswerArr[2] += 1;
    for i in range(1, 1000002) :
        if i not in ExistSet :
            continue;
        if IsVisitedAndStatus[i] == 0 and Indegree[i] > 0 :
            goThroughAndCheck(i, 2);
            AnswerArr[1] += 1;
    return AnswerArr

edges = [[4, 11], [1, 12], [8, 3], [12, 7], [4, 2], [7, 11], [4, 8], [9, 6], [10, 11], [6, 10], [3, 5], [11, 1], [5, 3], [11, 9], [3, 8]];
print(solution(edges));