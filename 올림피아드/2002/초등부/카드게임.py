import sys;
input = sys.stdin.readline;

Picked = [];
Colors = [];
Nums = [];
NumCntMapper = dict();
ColorCntMapper = dict();

for _ in range(5) :
    color, num = input().split();
    Picked.append((color, int(num)));
    Colors.append(color);
    Nums.append(num);

def sameNumCounter() :
    for num in Nums :
        NumCntMapper[int(num)] = Nums.count(num);
    rtnArr = [];
    for key, value in NumCntMapper.items() :
        rtnArr.append((key, value));
    rtnArr.sort(key = lambda x : (-x[1], -x[0]));
    rtnArr = rtnArr[ : 2];
    return rtnArr;

def sameColorCounter() :
    for color in Colors :
        ColorCntMapper[color] = Colors.count(color);
    rtnArr = [];
    for key, value in ColorCntMapper.items() :
        rtnArr.append((key, value));
    rtnArr.sort(key = lambda x : -x[1]);
    rtnArr = rtnArr[ : 1];
    return rtnArr;

def serialDecider() :
    sortedNums = sorted(Nums);
    isSerial = True;
    for i in range(1, len(sortedNums)) :
        if int(sortedNums[i]) != int(sortedNums[i - 1]) + 1 :
            isSerial = False;
            break;
    return isSerial;


numMapperArr = sameNumCounter();
colorMapperArr = sameColorCounter();
if colorMapperArr[0][1] == 5 and serialDecider() == True :
    print(900 + int(max(Nums)));
elif numMapperArr[0][1] == 4 :
    print(800 + numMapperArr[0][0]);
elif numMapperArr[0][1] == 3 and numMapperArr[1][1] == 2 :
    print(700 + numMapperArr[0][0] * 10 + numMapperArr[1][0]);
elif colorMapperArr[0][1] == 5 :
    print(600 + int(max(Nums)));
elif serialDecider() == True :
    print(500 + int(max(Nums)));
elif numMapperArr[0][1] == 3 :
    print(400 + numMapperArr[0][0]);
elif numMapperArr[0][1] == 2 and numMapperArr[1][1] == 2 :
    print(300 + numMapperArr[0][0] * 10 + numMapperArr[1][0]);
elif numMapperArr[0][1] == 2 :
    print(200 + numMapperArr[0][0]);
else :
    print(100 + int(max(Nums)));