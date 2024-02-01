Mod = 10007;
Tops = None;
d = None;
def solution(n, tops):
    global Tops;
    Tops = [0] + tops;
    d = [0] * ((2 * n + 1) + 1)
    d[1] = 1;
    if Tops[1] == 1 :
        d[2] = 3;
    else :
        d[2] = 2;
    for i in range(3, 2 * n + 2) :
        if i % 2 == 0 :
            if Tops[i // 2] == 1 :
                d[i] = (2*d[i - 1] + d[i - 2]) % Mod;
            else :
                d[i] = (d[i - 1] + d[i - 2]) % Mod;
        else :
            d[i] = (d[i - 1] + d[i - 2]) % Mod;

    return d[2 * n + 1];

n = 4;
tops = [1, 1, 0, 1];
print(solution(n, tops));