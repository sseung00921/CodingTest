import sys;
input = sys.stdin.readline;

A = input().rstrip();
B = input().rstrip();
Mapp = dict();
for i in range(0, len(A)) :
    tmp = 0;
    lenn = 0;
    for j in range(i, len(A)) :
        tmp += len(A)**(ord(A[j]) - ord('a'));
        lenn += 1;
        Mapp[tmp] = lenn;

Answer = 0;
for i in range(0, len(B)) :
    tmp = 0;
    for j in range(i, len(B)) :
        tmp += len(A)**(ord(B[j]) - ord('a'));
        if tmp in Mapp :
            Answer = max(Answer, Mapp[tmp]);

print(Answer);