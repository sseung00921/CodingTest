"""
혹시라 출제될 가능성이 있을까 싶어 정리해두는 접미사배열 알고리즘과 이 알고리즘의 가장 기본적인 응용 중 하나인 LCP 알고리즘이다.
"""

import sys;
input = sys.stdin.readline;
s = input().strip();

n = len(s)
suffixArr = [i for i in range(n)]
g = [0] * (n + 1) #순위
tg = [0] * (n + 1) #새로운 순위(순위를 갱신할 때 이용할 배열)

for i in range(n):
    g[i] = ord(s[i])

g[n] = -1
tg[suffixArr[0]] = 0
tg[n] = -1
t = 1

while t < n:
    suffixArr.sort(key=lambda x:(g[x], g[min(x + t, n)]))

    for i in range(1, n):
        p, q = suffixArr[i - 1], suffixArr[i]
        if g[p] != g[q] or g[min(p + t, n)] != g[min(q + t, n)]:
            tg[q] = tg[p] + 1
        else:
            tg[q] = tg[p]

    if tg[n - 1] == n - 1:
        break

    t = t * 2
    g = tg[:]

tmp = [-1] * n; #suffixArr의 idx와 value를 change한 배열, suffixArr의 value가 이 배열의 idx이고 idx가 value이다.
lcp = [-1] * n; #lcp[i] (단, i >= 1)은 suffixArr[i]와 suffixArr[i - 1]의 최장 공통 접두어 길이.
lcp[0] = 'x'; #i == 0일 때는 그냥 x로 표시.
for i in range(n) :
    tmp[suffixArr[i]] = i;
lenn = 0;
for i in range(n) :
    if tmp[i] > 0 :
        j = suffixArr[tmp[i] - 1];
        while j + lenn < n and i + lenn < n and s[j + lenn] == s[i + lenn] :
            lenn += 1;
        lcp[tmp[i]] = lenn;
        if lenn > 0 :
            lenn -= 1;

saForPrint = [e + 1 for e in suffixArr];
print(*saForPrint);
print(*lcp)