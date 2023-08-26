import sys;
input = sys.stdin.readline;
INF = str(sys.maxsize);
M = {};
M['1'] = '('; M['2'] = ')'; M['3'] = '{'; M['4'] = '}'; M['5'] = '['; M['6'] = ']';

def check(a, b) :
    if len(a) < len(b) :
        return a;
    elif len(a) > len(b) :
        return b;
    else :
        return min(a, b);

def translator(numStr) :
    tmpArr = [];
    for c in numStr :
        tmpArr.append(M[c]);
    return ''.join(tmpArr);

d = [INF] * 1001;
d[1] = '12';
d[2] = '34'
d[3] = '56';
for i in range(4, 1001) :
    if i % 2 == 0 :
        d[i] = check(d[i], '1' + d[i//2] + '2');
    if i % 3 == 0 :
        d[i] = check(d[i], '3' + d[i//3] + '4');
    if i % 5 == 0 :
        d[i] = check(d[i], '5' + d[i//5] + '6');
    for j in range(1, i) :
        d[i] = check(d[i], d[j] + d[i - j]);

T = int(input());
for _ in range(T) :
    N = int(input());
    print(translator(d[N]));