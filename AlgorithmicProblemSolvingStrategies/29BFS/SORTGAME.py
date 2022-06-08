from collections import deque;

N = 0;
DIST = dict();

def preCalc() :
    arr = [str(i) for i in range(0, N)];
    q = deque([''.join(arr)]);
    DIST[''.join(arr)] = 0;
    while q :
        now  = q.popleft();
        cost = DIST[now];
        for i in range(0, N) :
            for j in range(i + 2, N + 1) :
                part1 = now[ : i] if i > 0 else '';
                part2 = now[i : j];
                part3 = now[j : ] if j < N else '';
                part2 = part2[::-1];
                concated = part1 + part2 + part3;
                if concated not in DIST.keys() :
                    q.append(concated);
                    DIST[concated] = cost + 1;

def solve(data) :
    arr = [];
    for i in range(0, N) :
        smaller = 0;
        for j in range(0, N) :
            if int(data[j]) < int(data[i]) :
                smaller += 1;
        arr.append(str(smaller));
    return DIST[''.join(arr)];

tc = int(input());
while tc > 0 :
    N = int(input());
    data = list(map(int, input().split()));
    preCalc();
    print(solve(data));
    tc -= 1;