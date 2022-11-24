"""
이 이분 매칭 알고리즘을 기반으로 하는 네트워크 플로우 알고리즘은 백준 11378번 정답 소스 코드 참고.
이분 매칭 알고리즘은 완전히 이해하기에 상당히 복잡하다. 물론 최대한 그 원리를 머리에 담아보려는 시도도 의미가 있지만 마치 플로이드 알고리즘을 사용할 때 그러하듯
이 알고리즘이 해낼 수 있는 퍼포먼스를 정확히 인지하는 것이 중요하고 문제를 풀 때
이 알고리즘이 반드시 필요한 순간을 캐치해내는 능력과 그 때 이 알고리즘을 적절히 사용하는 능력이 더 중요하다 할 수 있겠다.
"""

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