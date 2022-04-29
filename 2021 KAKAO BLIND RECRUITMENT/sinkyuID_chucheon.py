def makeIdPure(new_id) :
    rtnId = ''
    for c in new_id :
        if c.isnumeric() or c.isalpha() or c == '-' or c == '.' or c == '_' :
            rtnId += c;
    return rtnId;

def makeDoubleMachimpyoOnce(new_id) :
    while True :
        if new_id.find("..") == - 1 :
            break;
        new_id = new_id.replace("..", ".");
    return new_id;

def clearEachSideMachimpyo(new_id) :
    if len(new_id) > 0 and new_id[0] == '.' :
        new_id = new_id[1 : ];
    if len(new_id) > 0 and new_id[-1] == '.' :
        new_id = new_id[ : -1];
    return new_id;

def solution(new_id):
    new_id = new_id.lower();
    new_id = makeIdPure(new_id);
    new_id = makeDoubleMachimpyoOnce(new_id);
    new_id = clearEachSideMachimpyo(new_id);
    if len(new_id) == 0 :
        new_id = 'a';
    if len(new_id) >= 16 :
        new_id = new_id[ : 15];
        new_id = clearEachSideMachimpyo(new_id);
    if len(new_id) <= 2 :
        lastChar = new_id[-1];
        while len(new_id) < 3 :
            new_id += lastChar;

    return new_id;

new_id = "=.="
print(solution(new_id));