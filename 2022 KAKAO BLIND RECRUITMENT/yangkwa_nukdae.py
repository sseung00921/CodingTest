N = 0;
Info = None;
Graph = None;
MaxLamb = 0;

def dfs(nowNode, lamb, wolf, path) :
    global MaxLamb;

    if Info[nowNode] == 0 :
        lamb += 1;
    else :
        wolf += 1;

    if wolf >= lamb :
        return;

    for p in path :
        for next in Graph[p] :
            if next not in path :
                path.append(next);
                dfs(next, lamb, wolf, path);
                path.pop();

    MaxLamb = max(MaxLamb, lamb)
    return;

def solution(info, edges):
    global N;
    global Info;
    global Graph;
    Info = info;
    N = len(info)
    graph = [[] for _ in range(N)];
    Graph = graph;
    for edge in edges :
        parent, child = edge;
        Graph[parent].append(child);
        Graph[child].append(parent);
    dfs(0, 0, 0, [0]);
    return MaxLamb;

info = [0,0,1,1,1,0,1,0,1,0,1,1];
edges = [[0,1],[1,2],[1,4],[0,8],[8,7],[9,10],[9,11],[4,3],[6,5],[4,6],[8,9]];
print(solution(info, edges));
info = [0,1,0,1,1,0,1,0,0,1,0];
edges = [[0,1],[0,2],[1,3],[1,4],[2,5],[2,6],[3,7],[4,8],[6,9],[9,10]];
print(solution(info, edges));