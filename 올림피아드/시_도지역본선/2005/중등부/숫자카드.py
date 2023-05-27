import sys;
input = sys.stdin.readline;

n = input().rstrip();
sett = set();
for i in range(1, 35) :
    sett.add(str(i));
d = [[-1] * (len(n) + 1) for _ in range(35)];

def dfs(head, remainLen) :
    if head == '' :
        if d[0][remainLen] != -1 :
            return d[0][remainLen];
    else :
        if d[int(head)][remainLen] != -1 :
            return d[int(head)][remainLen]

    if remainLen == 0 :
        d[int(head)][remainLen] = 1;
        return d[int(head)][remainLen];

    tmp = 0;
    if remainLen > 1 and n[-(remainLen - 1)] == '0' :
        nextHead = n[-remainLen] + n[-(remainLen - 1)];
        tmp += dfs(nextHead, remainLen - 2);
    else :
        if remainLen > 0 and n[-remainLen] != '0' :
            nextHead = n[-remainLen];
            tmp += dfs(nextHead, remainLen - 1);
        if remainLen > 1 and n[-(remainLen - 1)] != '0':
            nextHead = n[-remainLen] + n[-(remainLen - 1)];
            if nextHead in sett :
                tmp += dfs(nextHead, remainLen - 2);

    if head == '' :
        head = 0;
    d[int(head)][remainLen] = tmp;
    return d[int(head)][remainLen];

print(dfs('', len(n)));
