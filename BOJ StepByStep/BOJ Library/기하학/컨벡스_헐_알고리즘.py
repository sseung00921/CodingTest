"""2차원 좌표상에 서로 다른 점 N개가 주어졌을 때 그 점들 중 임의의 점들을 이어 그 N개의 모든 점들을 전부 포함하는 다각형을 만들기 위해 이어야 할 점들의 최소 갯수를 구하는
알고리즘이다. 기하학적 깊은 내용을 다루고 있으므로 그저 여기서는 그런 함수 자체만 저장해두고 넘어가도록 한다."""

import sys;
input = sys.stdin.readline;

def inclination(p1, p2):
    return p2[0] - p1[0], p2[1] - p1[1]

def ccw(p1, p2, p3):
    v, u = inclination(p1, p2), inclination(p2, p3)
    if v[0] * u[1] > v[1] * u[0]:
        return True
    return False

def convex_hull(positions):
    convex = list()
    for p3 in positions:
        while len(convex) >= 2:
            p1, p2 = convex[-2], convex[-1]
            if ccw(p1, p2, p3):
                break
            convex.pop()
        convex.append(p3)

    return len(convex)

n, answer = int(input()), -2
positions = list()
for i in range(n):
    positions.append(list(map(int, input().split())))

positions = sorted(positions, key=lambda pos:(pos[0], pos[1]))
answer += convex_hull(positions)

positions.reverse()
answer += convex_hull(positions)
print(answer)