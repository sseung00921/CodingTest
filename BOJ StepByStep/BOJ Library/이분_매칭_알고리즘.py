import sys;
input = sys.stdin.readline;
n, m = map(int, input().split())
employees = [[] for _ in range(n + 1)];
whoWorks = [0] * (m + 1);

def dfs(start) :
    #한번 다른 일 가능한지 물어본 적이 있다면 그냥 패스.
    if visited[start] == True :
        return False;

    #이 직원은 이제 한번 물어본 적이 있는 직원이 되는 것.
    visited[start] = True;

    #자기가 가능한 일 중 다른 일 가능한지 찾아본다. 이 과정에서 또 다른 일하는 직원들에게 연쇄적으로 물어보며 찾아본다.
    for canDo in employees[start] :
        if whoWorks[canDo] == 0 or dfs(whoWorks[canDo]) :
            whoWorks[canDo] = start;
            return True;

    return False;


for i in range(1, n + 1) :
    canDo = list(map(int, input().split()))
    for j in range(1, len(canDo)) :
        employees[i].append(canDo[j]);

cnt = 0;
for i in range(1, n + 1) :
    visited = [False] * (n + 1);
    if dfs(i) :
        cnt += 1;

print(cnt);