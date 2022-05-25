tc = int(input());
IDX = 0;
DATA = None;
def dfs() :
    global IDX;
    if DATA[IDX] == 'b' or DATA[IDX] == 'w' :
        rtnStr = DATA[IDX];
        IDX += 1;
        return rtnStr;

    IDX += 1;
    rtnStr = '';
    upperLeft = dfs();
    upperRight = dfs();
    lowerLeft = dfs();
    lowerRight = dfs();
    rtnStr = 'x' + lowerLeft + lowerRight + upperLeft + upperRight;

    return rtnStr;

while tc > 0 :
    data = input();
    DATA = data;
    print(dfs());
    IDX = 0;
    tc -= 1;