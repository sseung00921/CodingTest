import math

n = int(input())

#원 간의 포함여부를 구하는 함수
def isC2ExistInC1(c1, c2) :
    r1, x1, y1, id1 = c1;
    r2, x2, y2, id2 = c2;
    if (r1 - r2) > math.sqrt(((x2 - x1)**2) + ((y2 - y1)**2)) :
        return True;
    return False;

for _ in range(n):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    distance = math.sqrt((x1-x2)**2 + (y1-y2)**2)  # 두 원의 거리 (원의방정식활용)
    if distance == 0 and r1 == r2 :  # 두 원이 동심원이고 반지름이 같을 때
        print(-1)
    elif abs(r1-r2) == distance or r1 + r2 == distance:  # 내접, 외접일 때
        print(1)
    elif abs(r1-r2) < distance < (r1+r2) :  # 두 원이 서로다른 두 점에서 만날 때
        print(2)
    else:
        print(0)  # 그 외에