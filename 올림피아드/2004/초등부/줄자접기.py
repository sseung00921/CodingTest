import sys;
input = sys.stdin.readline;

n = int(input());

red = list(map(int, input().split())); red.sort();
blue = list(map(int, input().split())); blue.sort();
yellow = list(map(int, input().split())); yellow.sort();

midRed = (red[0] + red[1]) / 2;
midN  = n / 2;
if midRed < midN :
    for i in range(0, 2) :
        if blue[i] < midRed :
            blue[i] = midRed - blue[i];
        else :
            blue[i] -= midRed;
        if yellow[i] < midRed :
            yellow[i] = midRed - yellow[i];
        else :
            yellow[i] -= midRed;
    n -= midRed;
elif midRed >= midN :
    for i in range(0, 2) :
        if blue[i] > midRed :
            blue[i] = midRed - (blue[i] - midRed);
        if yellow[i] > midRed :
            yellow[i] = midRed - (yellow[i] - midRed);
    n = midRed;

if blue[0] != blue[1] :
    blue.sort(); yellow.sort();
    midBlue = (blue[0] + blue[1])/ 2;
    midN = n / 2;
    if midBlue < midN :
        for i in range(0, 2) :
            if yellow[i] < midBlue :
                yellow[i] = midBlue - yellow[i];
            else :
                yellow[i] -= midBlue;
        n -= midBlue;
    elif midBlue >= midN :
        for i in range(0, 2) :
            if yellow[i] > midBlue :
                yellow[i] = midBlue - (yellow[i] - midBlue);
        n = midBlue;

if yellow[0] != yellow[1] :
    yellow.sort();
    midYellow = (yellow[0] + yellow[1]) / 2;
    midN = n / 2;
    if midYellow < midN :
        n -= midYellow;
    elif midYellow >= midN :
        n = midYellow;

print(n);