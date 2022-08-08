import math;

n = int(input());
squtt = int(math.sqrt(n));
d = 2;

while d <= squtt and n != 1 :
    if n % d == 0 :
        n //= d;
        print(d);
    else :
        d += 1;

if n > 1 :
    print(n);