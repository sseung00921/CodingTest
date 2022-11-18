"""
플로이드의 각 노드간의 최단 경로까지 출력하는 문제는 백준 11780번 정답을 참고한다. 참고로 그 문제는 같은 노드로 돌아오는 최단 경로는 그 경로가 존재해도 0으로 출력하라는 조금은
이상한 특이조건이 있어서 해당 문제의 정답은 그 특이조건을 고려한 것이다. 더 일반적인 상황인 자기자신으로 돌아오는 최단경로까지도 존재하면 출력하는 알고리즘은 해당 문제의 가장 첫번째로
제출된 오답 코드를 참고한다.
"""

import sys;
INF = int(1e9);
n = int(sys.stdin.readline());
m = int(sys.stdin.readline());

Graph = [[INF] * (n + 1) for _ in range(n + 1)];

for _ in range(m) :
    a, b, cost = map(int, sys.stdin.readline().split());
    Graph[a][b] = min(Graph[a][b], cost);

for i in range(1, n + 1) :
    for j in range(1, n + 1) :
        if i == j :
            Graph[i][j] = 0;

for k in range(1, n + 1) :
    for i in range(1, n + 1) :
        for j in range(1, n + 1) :
            Graph[i][j] = min(Graph[i][j], Graph[i][k] + Graph[k][j]);

for i in range(1, n + 1) :
    print(*Graph[i][1 : ]);