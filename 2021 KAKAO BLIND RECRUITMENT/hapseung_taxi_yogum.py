def solution(n, s, a, b, fares):
    answer = int(1e9);
    graph = [[int(1e9)] * (n + 1) for _ in range(n + 1)];
    for i in range(1, n + 1) :
        graph[i][i] = 0;
    for fare in fares :
        city1, city2, cost = fare;
        graph[city1][city2] = cost;
        graph[city2][city1] = cost;

    for k in range(1, n + 1) :
        for i2 in range(1, n + 1) :
            for j in range(1, n + 1) :
                graph[i2][j] = min(graph[i2][j], graph[i2][k] + graph[k][j]);

    for i3 in range(1, n + 1) :
        answer = min(answer, graph[s][i3] + graph[i3][a] + graph[i3][b]);
    return answer

n = 6
s = 4
a = 6
b = 2
fares = [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]];
print(solution(n, s, a, b, fares));