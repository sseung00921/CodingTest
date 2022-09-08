#--------순서 정보가 일부만 주어졌을 때 가능한 전체 순서 구하기----------------
#이를테면, 키 순서대로 아이들을 정렬하는 데 a, b, c, d, e, f, g, h 이렇게 8명 중 a < e, f < g, d < h, c < a 이런 식으로 일부 아이 쌍들의 키 비교 결과 정보만 주어졌을 때 가능한 키 순서 정렬 결과를 찾는 문제.
#가능한 전체 순서는 여러 개일 수 있고 그 중에 아무거나 하나만 찾으면 되는 경우일 수 있다.
n, m = map(int, input().split());
Indegree = [0] * (n + 1);
covered = [False] * (n + 1);
Graph = [[] for _ in range(n + 1)];

for _ in range(m) :
    a, b = map(int, input().split());
    Indegree[b] += 1;
    Graph[a].append(b);

answerList = [];
while len(answerList) < n :
    for i in range(1, n + 1) :
        if Indegree[i] == 0 and not covered[i] :
            answerList.append(i);
            covered[i] = True;
            for j in Graph[i] :
                Indegree[j] -= 1;
            break;

print(*answerList)