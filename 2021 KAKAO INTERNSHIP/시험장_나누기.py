import sys;
sys.setrecursionlimit(10**5);

p = [];
l = [];
r = [];
Num = None;
root = 0;
N = 0;

def dfs(root, limit) :
    if l[root] == -1 and r[root] == -1 :
        return Num[root], 1;
    elif l[root] != -1 and r[root] == -1 :
        lGroupSum, lGroupCnt = dfs(l[root], limit);
        if Num[root] + lGroupSum <= limit :
            return Num[root] + lGroupSum, lGroupCnt;
        else :
            return Num[root], lGroupCnt + 1;
    elif l[root] == -1 and r[root] != -1 :
        rGroupSum, rGroupCnt = dfs(r[root], limit);
        if Num[root] + rGroupSum <= limit :
            return Num[root] + rGroupSum, rGroupCnt;
        else :
            return Num[root], rGroupCnt + 1;
    elif l[root] != -1 and r[root] != -1 :
        lGroupSum, lGroupCnt = dfs(l[root], limit);
        rGroupSum, rGroupCnt = dfs(r[root], limit);
        if Num[root] + lGroupSum + rGroupSum <= limit :
            return Num[root] + lGroupSum + rGroupSum, lGroupCnt + rGroupCnt - 1;
        elif Num[root] + lGroupSum <= limit or Num[root] + rGroupSum <= limit :
            return Num[root] + min(lGroupSum, rGroupSum), lGroupCnt + rGroupCnt;
        else :
            return Num[root], lGroupCnt + rGroupCnt + 1;

    return;

def solution(k, num, links):
    global root;
    global N; N = len(num);
    global Num; Num = num;
    for _ in range(N) :
        p.append(-1);
    for i in range(N) :
        left, right = links[i];
        l.append(left);
        r.append(right);
        if left != -1 :
            p[left] = i;
        if right != -1 :
            p[right] = i;
    for i in range(N) :
        if p[i] == -1 :
            root = i;
            break;

    start = max(num);
    end = sum(num);
    answer = end;
    while start <= end :
        mid = (start + end) // 2;
        groupCnt = dfs(root, mid)[1];
        if groupCnt > k :
            start = mid + 1;
        elif groupCnt <= k :
            answer = min(answer, mid);
            end = mid - 1;
    return answer

k = 3
num = [12, 30, 1, 8, 8, 6, 20, 7, 5, 10, 4, 1];
links = [[-1, -1], [-1, -1], [-1, -1], [-1, -1], [8, 5], [2, 10], [3, 0], [6, 1], [11, -1], [7, 4], [-1, -1], [-1, -1]];
print(solution(k, num, links));