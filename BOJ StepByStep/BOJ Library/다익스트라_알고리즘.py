"""최단 경로의 비용 뿐만 아니라 최단 경로에서 시작점부터 도착점까지 거쳐가는 모든 노드들의 번호까지 풀로 출력하는 개량된 다익스트라 알고리즘이 필요하다면
백준 11779번에 내가 제출한 소스 코드를 참고할 것."""
import heapq;
INF = int(1e9);

v, e = map(int, input().split())
start = int(input());
graph = [[] for _ in range(v + 1)];
d = [INF] * (v + 1);
for _ in range(e) :
    a, b, c = map(int, input().split());
    graph[a].append((c, b));

d[start] = 0;
q = [(0, start)];

while q :
    dist, now = heapq.heappop(q);
    if dist > d[now] :
        continue;
    for i in graph[now] :
        nDist = d[now] + i[0];
        if nDist < d[i[1]] :
            d[i[1]] = nDist;
            heapq.heappush(q, (nDist, i[1]));

for i in range(1, v + 1) :
    if d[i] == INF :
        print("INF");
    else :
        print(d[i]);