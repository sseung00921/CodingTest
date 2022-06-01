N = 0;
MAX_LONG_DISTANCE = 0;

class Fortress :
    def __init__(self, id, x, y, r, parent, chlidren) :
        self.id = id;
        self.x = x;
        self.y = y;
        self.r = r;
        self.parent = parent;
        self.chlidren = chlidren;

def enclose(encloser, enclosed) :
    if enclosed.r < encloser.r and abs(encloser.x - enclosed.x)**2 + abs(encloser.y - enclosed.y)**2 + enclosed.r**2 < encloser.r**2 :
        return True;
    return False;

def isChild(parent, child) :
    if enclose(parent, child) == False :
        return False;
    for otherFortress in fortressList :
        if otherFortress.id != parent.id and otherFortress.id != child.id and enclose(parent, otherFortress) and enclose(otherFortress, child) :
            return False;
    return True;


def makeTree(rootFortress) :
    for fortress in fortressList :
        if fortress.id == rootFortress.id :
            continue;
        if isChild(rootFortress, fortress) :
            fortress.parent = rootFortress;
            rootFortress.chlidren.append(makeTree(fortress));
    return rootFortress;

def getHeight(rootFortress) :
    global MAX_LONG_DISTANCE;

    if len(rootFortress.chlidren) == 0 :
        return 0;

    height = 0;
    childrenHeightList = [];
    for child in rootFortress.chlidren :
        childHeight = getHeight(child)
        childrenHeightList.append(childHeight)
        height = max(height, childHeight + 1);

    childrenHeightList.sort();
    if len(childrenHeightList) >= 2 :
        MAX_LONG_DISTANCE = max(MAX_LONG_DISTANCE, childrenHeightList[-1] + childrenHeightList[-2] + 2);

    return height;

tc = int(input());
while tc > 0 :
    N = int(input());
    fortressList = [];
    id = 0;
    for i in range(N) :
        x, y, r = map(int, input().split());
        fortressList.append(Fortress(id, x, y, r, None, []));
        id += 1;
    makeTree(fortressList[0]);

    MAX_LONG_DISTANCE = 0;
    height = getHeight(fortressList[0]);
    print(max(MAX_LONG_DISTANCE, height));
    tc -= 1;
