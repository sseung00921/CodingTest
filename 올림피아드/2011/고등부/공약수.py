import sys;
input = sys.stdin.readline;
import math;

gcd, lcm = map(int, input().split());
aTimesB = lcm * gcd;

startNum = int(math.sqrt(aTimesB));

for num in range(startNum, 0, -1) :
    if aTimesB % num == 0 and math.gcd(num, aTimesB // num) == gcd :
        print(num, aTimesB // num);
        break;
