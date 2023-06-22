import sys;
input = sys.stdin.readline;

N, L = map(int, input().split());
data = [None];
for _ in range(N) :
    length, dir = map(int, input().split());
    if dir == 0 :
        data.append(((0, length), dir));
    elif dir == 1 :
        data.append(((L - length, L), dir));

def checkCanUp(bot, top) :
    botL, botR = bot;
    topL, topR = top;
    if botR < topL :
        return False;
    if botL > topR :
        return False;
    return True;

def getLRgivenT(sec, bar) :
    barRange = bar[0];
    dir = bar[1];
    barL, barR = barRange;
    length = barR - barL
    period = (L - length) * 2;
    if period == 0 :
        return 0, L;
    sec = sec % period;
    if dir == 0 :
        startL = 0; startR = length;
        endL = L - length; endR = L;
        if sec == L - length :
            return endL, endR;
        else :
            if sec < L - length :
                return startL + sec, startR + sec;
            elif sec > L - length :
                sec = sec - (L - length);
                return endL - sec, endR - sec;
    elif dir == 1 :
        startL = L - length; startR = L;
        endL = 0; endR = length;
        if sec == L - length :
            return endL, endR;
        else :
            if sec < L - length :
                return startL - sec, startR - sec;
            elif sec > L - length :
                sec = sec - (L - length);
                return endL + sec, endR + sec;
    return;

NowFloor = 1;
NowElapsedSec = 0;
while True :
    while True :
        if NowFloor == N :
            break;
        NowFloorRange = getLRgivenT(NowElapsedSec, data[NowFloor]);
        NextFloorRange = getLRgivenT(NowElapsedSec, data[NowFloor + 1]);
        if checkCanUp(NowFloorRange, NextFloorRange) :
            NowFloor += 1;
        else :
            break;
    if NowFloor == N :
        break;
    NowElapsedSec += 1;

print(NowElapsedSec);