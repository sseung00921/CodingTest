"""CCW 알고리즘의 CCW는 CounterClockWise의 약자이다. 즉 이 알고리즘은 이름 그대로 세 점과 세 점을 잇는 순서(p1-p2를 먼저 잇고 p2-p3을 잇는다)가
주어졌을 때 p1에서 p3까지 반시계 방향으로 선분이 이어지는지 혹은 시계방향으로 선분이 이어지는지 아니면 일직선으로 이어지는 지를 판별하는 알고리즘이다."""


data = [];
for _ in range(3) :
    a, b = map(int, input().split());
    data.append((a, b));

def ccw(p1, p2, p3) :
    x1, y1 = p1;
    x2, y2 = p2;
    x3, y3 = p3;
    return (x1*y2 + x2*y3 + x3*y1) - (x2*y1 + x3*y2 + x1*y3);

result = ccw(data[0], data[1], data[2]);

if result < 0 :
    print(-1) #시계 방향
elif result > 0 :
    print(1) #반시계 방향
elif result == 0 :
    print(0) #일직선