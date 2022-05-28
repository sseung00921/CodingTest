W = '';
S = '';
cache = [[-1] * 110 for _ in range(110)];

def match(w, s) :
    if w > len(W) or s > len(S) :
        return False;

    if cache[w][s] != -1 :
        return cache[w][s];

    while w < len(W) and s < len(S) :
        if W[w] == '?' or W[w] == S[s] :
            return match(w + 1, s + 1);
        else :
            break;

    if w == len(W) :
        cache[w][s] = (s == len(S));
        return cache[w][s];

    if w < len(W) and W[w] == '*' :
        if match(w + 1, s) or match(w, s + 1) :
            cache[w][s] = True;
            return cache[w][s];

    cache[w][s] = 0;
    return cache[w][s];

tc = int(input());
while tc > 0 :
    w = input();
    W = w;
    n = int(input());
    data = [];
    for _ in range(n) :
        data.append(input());
    answer = [];
    for s in data :
        cache = [[-1] * 110 for _ in range(110)]
        S = s;
        if match(0, 0) :
            answer.append(s);
    answer.sort();
    for matched in answer :
        print(matched);
    tc -= 1;