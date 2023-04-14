import sys;
input = sys.stdin.readline;

n = int(input());
data = list(map(int, input().split()));
data.sort();

answer1 = data[(n - 1) // 2]

powSum = 0;
for i in range(n) :
    powSum += data[i] ** 2;

summ = sum(data);

minVariance = -1;
answer2 = -1;
for k in range(1, 10001) :
    val = powSum - 2*summ*k + n*(k**2);
    if minVariance == -1 or val < minVariance :
        minVariance = val;
        answer2 = k;

print(answer1, answer2);