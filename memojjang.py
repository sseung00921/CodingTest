import sys;
input = sys.stdin.readline;

T = input().rstrip();
P = input().rstrip();
pi = [0] * len(P);

j = 0;
for i in range(1, len(P)) :
    while j > 0 and P[j] != P[i] :
        j = pi[j - 1];

    if P[j] == P[i] :
        j += 1;
        pi[i] = j;

j = 0;
count = 0;
answer = [];
for i in range(0, len(T)) :
    while j > 0 and T[i] != P[j] :
        j = pi[j - 1];

    if T[i] == P[j] :
        if j == len(P) - 1 :
            count += 1;
            answer.append(i - len(P) + 2);
            j = pi[j];
        else :
            j += 1;

print(count); #P가 T내에서 몇번 일치하는 구간이 나타나는지.
print(*answer); #일치하는 구간이 나타날 때마다 그 구간의 시작점의 T 인덱스.