d = [[int(1e9)] * 2 for _ in range(300001)];
tree = [[] for _ in range(300001)];

def dfs(sales, node) :
    d[node][0] = 0;
    d[node][1] = sales[node - 1];

    if not tree[node] :
        return;

    extra = int(1e9);

    for child in tree[node] :
        dfs(sales, child);
        if d[child][0] < d[child][1] :
            d[node][0] += d[child][0];
            d[node][1] += d[child][0];
            extra = min(extra, d[child][1] - d[child][0]);
        else :
            d[node][0] += d[child][1];
            d[node][1] += d[child][1];
            extra = 0;

    d[node][0] += extra;


def solution(sales, links):
    for link in links :
        parent, child = link;
        tree[parent].append(child);
    dfs(sales, 1); #1 is root;
    return min(d[1][0], d[1][1]);

sales = [14, 17, 15, 18, 19, 14, 13, 16, 28, 17];
links = [[10, 8], [1, 9], [9, 7], [5, 4], [1, 5], [5, 10], [10, 6], [1, 3], [10, 2]];
print(solution(sales, links));
print(d);