import sys;
input = sys.stdin.readline;

m = dict();

n = int(input());
data = [-1] + list(map(int, input().split()));

for i in range(1, n + 1) :
    m[i] = data[i];

def gcd(a, b) :
    while b != 0 :
        a, b = b, a%b;
    return a;

def lcm(a, b) :
    return a*b // gcd(a, b);

Answer = 1;
Visited = [0] * (n + 1);
for i in range(1, n + 1) :
    if Visited[i] :
        continue;
    Visited[i] = 1;
    cnt = 1;
    next = m[i];
    while not Visited[next] :
        cnt += 1;
        Visited[next] = 1;
        next = m[next];
    Answer = lcm(Answer, cnt);

print(Answer);
