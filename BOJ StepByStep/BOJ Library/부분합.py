import sys;
n, m = map(int, sys.stdin.readline().split());

data = list(map(int, sys.stdin.readline().split()));

partialSum = [0] * (n + 1);

for i in range(1, len(data) + 1) :
    if i == 1 :
        partialSum[1] = data[0];
    else:
        partialSum[i] = data[i - 1] + partialSum[i - 1];

for _ in range(m) :
    a, b = map(int, sys.stdin.readline().split());
    answer = partialSum[b] - partialSum[a - 1];
    print(answer);