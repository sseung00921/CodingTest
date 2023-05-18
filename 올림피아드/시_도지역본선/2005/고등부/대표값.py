import sys;
input = sys.stdin.readline;

summ = 0;
m = dict();

for _ in range(10) :
    n = int(input());
    if n not in m :
        m[n] = 1;
    else :
        m[n] += 1;
    summ += n;

print(int(summ / 10));
mostRepeatedCnt = -1;
mostRepeatedVal = 1;
for k, v in m.items() :
    if v > mostRepeatedCnt :
        mostRepeatedCnt = v;
        mostRepeatedVal = k;
print(mostRepeatedVal);