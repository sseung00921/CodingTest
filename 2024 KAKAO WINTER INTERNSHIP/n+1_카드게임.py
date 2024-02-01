N = 0;
Answer = 1;
Cards = None;

def solution(coin, cards):
    global N; global Cards;
    Cards = cards;
    N = len(cards);
    VisitSet = set();
    for i in range(N // 3) :
        VisitSet.add(cards[i]);
    startCanGoCnt = 0;
    for e in VisitSet :
        if N + 1 - e in VisitSet :
            startCanGoCnt += 1;
    startIdx = (N // 3);
    startCanGoCnt //= 2;
    canGo = 1 + startCanGoCnt;
    nowCoin = coin;
    RemainSet = set();
    while True :
        destIdx = startIdx + (2 * canGo);
        canGo = 0;
        if destIdx == startIdx or destIdx > N :
            Answer = (destIdx - (N // 3)) // 2;
            break;
        for i in range(startIdx, destIdx) :
            if N + 1 - Cards[i] in VisitSet :
                if nowCoin > 0 :
                    nowCoin -= 1;
                    canGo += 1;
                    VisitSet.add(Cards[i]);
                elif nowCoin == 0 :
                    break;
            else :
                RemainSet.add(Cards[i]);
        if canGo == 0 :
            pairA, pairB = None, None;
            IsTwoExist = False;
            for e in RemainSet :
                if N + 1 - e in RemainSet :
                    pairA = e;
                    pairB = N + 1 - e;
                    IsTwoExist = True;
                    break;
            if IsTwoExist and nowCoin >= 2 :
                RemainSet.remove(pairA);
                RemainSet.remove(pairB);
                canGo += 1;
                VisitSet.add(pairA);
                VisitSet.add(pairB);
                nowCoin -= 2;

        startIdx = destIdx;

    return Answer;

coin = 4;
cards = [3, 6, 7, 2, 1, 10, 5, 9, 8, 12, 11, 4];
print(solution(coin, cards));

Answer = -1;

coin = 3;
cards = [1, 2, 3, 4, 5, 8, 6, 7, 9, 10, 11, 12];
print(solution(coin, cards));

Answer = -1;

coin = 2;
cards = [5, 8, 1, 2, 9, 4, 12, 11, 3, 10, 6, 7];
print(solution(coin, cards));

Answer = -1;

coin = 10;
cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18];
print(solution(coin, cards));