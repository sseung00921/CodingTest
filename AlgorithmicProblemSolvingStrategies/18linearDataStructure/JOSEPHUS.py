tc = int(input());

while tc > 0 :
    n, k = map(int, input().split());
    captives = [i for i in range(n)]; #1번병사부터 죽는다지만 구현 편의를 위해 0번부터 죽는다 치고 모든 병사 번호들을 -1한다.
    turnToDead = 0;
    while len(captives) > 2 :
        del captives[turnToDead]
        turnToDead += (k - 1);
        if turnToDead >= len(captives) :
            turnToDead %= len(captives);
    for i in range(len(captives)) :
        if i == (len(captives) - 1) :
            print(captives[i] + 1);
            break;
        print(captives[i] + 1, end = ' ');
    tc -= 1;