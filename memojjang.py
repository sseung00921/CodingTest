import sys;
input = sys.stdin.readline;
n, m = map(int, input().split())

def twoCounter(num) :
    two = 0;
    while num != 0 :
        num //= 2;
        two += num;
    return two;

def fiveCounter(num) :
    five = 0;
    while num != 0 :
        num //= 5;
        five += num;
    return five;

print(min(twoCounter(n) - twoCounter(n - m) - twoCounter(m), fiveCounter(n) - fiveCounter(n - m) - fiveCounter(m)));