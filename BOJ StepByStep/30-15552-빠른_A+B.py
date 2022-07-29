import sys;

tc = int(sys.stdin.readline());

while tc > 0 :
    a, b = map(int, sys.stdin.readline().split());
    print(a + b);
    tc -= 1