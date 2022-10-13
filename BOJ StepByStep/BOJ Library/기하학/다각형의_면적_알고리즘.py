"""(x,y) 좌표 점이 N개 주어질 때 그 점들을 잇는 도형의 넓이를 구하는 알고리즘. 신발끈 정리라는 것을 이용하는 데 이해는 못하더라도 공식 자체는 알고 있자."""
import sys;
input = sys.stdin.readline;
n = int(input());
xArr = [];
yArr = [];
for _ in range(n) :
    x, y = map(int, input().split());
    xArr.append(x);
    yArr.append(y);

xArr = xArr + [xArr[0]];
yArr = yArr + [yArr[0]];

answer = 0;
for i in range(n) :
    answer += xArr[i + 1]*yArr[i] - yArr[i + 1]*xArr[i];

print(format(round(abs(answer / 2), 1), ".1f"));