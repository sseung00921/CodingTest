import sys;

input = sys.stdin.readline;
Board = [];
for _ in range(10) :
    Board.append(input().rstrip());

def emptyOrOnePoint(n, isGaro) :
    if isGaro :
        IsEmpty = True;
        OnePoint = -1
        for j in range(10) :
            if Board[n][j] == '1' :
                IsEmpty = False;
                if OnePoint == -1 :
                    OnePoint = (n, j);
                else :
                    return False;
        if IsEmpty :
            return True;
        else :
            return OnePoint;
    else :
        IsEmpty = True;
        OnePoint = -1
        for i in range(10) :
            if Board[i][n] == '1' :
                IsEmpty = False;
                if OnePoint == -1 :
                    OnePoint = (i, n);
                else :
                    return False;
        if IsEmpty :
            return True;
        else :
            return OnePoint;

def oneInLimit(n, start, end, isGaro) :
    if isGaro :
        for j in range(0, start) :
            if Board[n][j] == '1' :
                return False;
        for j in range(start, end + 1) :
            if Board[n][j] == '0' :
                return False;
        for j in range(end + 1, 10) :
            if Board[n][j] == '1' :
                return False;
    else :
        for i in range(0, start) :
            if Board[i][n] == '1' :
                return False;
        for i in range(start, end + 1) :
            if Board[i][n] == '0' :
                return False;
        for i in range(end + 1, 10) :
            if Board[i][n] == '1' :
                return False;
    return True;

def checkOob(start, end) :
    if start < 0 or start >= 10 or end < 0 or end >= 10 :
        return False;
    return True;

def checkIfOnlyOne() :
    cnt = 0;
    for i in range(10) :
        for j in range(10) :
            if Board[i][j] == '1' :
                cnt += 1;
    if cnt == 1 :
        return True;
    else :
        return False;

#case1
AnswerArr = [];
isSatisfying = True;
sRow = -1; sCol = -1;
for i in range(10) :
    if i == 9 :
        isSatisfying = False;
    if emptyOrOnePoint(i, True) == True :
        continue;
    elif emptyOrOnePoint(i, True) == False :
        isSatisfying = False;
        break;
    else :
        sRow, sCol = emptyOrOnePoint(i, True);
        AnswerArr.append((sRow, sCol));
        break;
fromNowShouldEmpty = False;
fromNowShouldEmptyStart = -1;
if not (sRow == -1 and sCol == -1) :
    start = sCol;
    end = sCol + 1;
    for i in range(sRow + 1, 10) :
        if not checkOob(start, end) :
            if emptyOrOnePoint(i, True) == True :
                fromNowShouldEmpty = True;
                fromNowShouldEmptyStart = i + 1;
            break;
        if oneInLimit(i, start, end, True) :
            if i == 9 :
                AnswerArr.append((i, start));
                AnswerArr.append((i, end));
            end += 1;
        elif emptyOrOnePoint(i, True) == True :
            AnswerArr.append((i - 1, start));
            AnswerArr.append((i - 1, end - 1));
            fromNowShouldEmpty = True;
            fromNowShouldEmptyStart = i + 1;
            break;
        else :
            isSatisfying = False;
            break;
if fromNowShouldEmpty :
    for i in range(fromNowShouldEmptyStart, 10) :
        if emptyOrOnePoint(i, True) != True :
            isSatisfying = False;
            break;
if checkIfOnlyOne() :
    isSatisfying = False;
if len(AnswerArr) != 3 :
    isSatisfying = False;
if isSatisfying :
    AnswerArr.sort();
    for e in AnswerArr :
        i, j = e;
        print(i + 1, j + 1);
    sys.exit();

#case2
AnswerArr = [];
isSatisfying = True;
sRow = -1; sCol = -1;
for i in range(10) :
    if i == 9 :
        isSatisfying = False;
    if emptyOrOnePoint(i, True) == True :
        continue;
    elif emptyOrOnePoint(i, True) == False :
        isSatisfying = False;
        break;
    else :
        sRow, sCol = emptyOrOnePoint(i, True);
        AnswerArr.append((sRow, sCol));
        break;
fromNowShouldEmpty = False;
fromNowShouldEmptyStart = -1;
if not (sRow == -1 and sCol == -1) :
    start = sCol - 1;
    end = sCol;
    for i in range(sRow + 1, 10) :
        if not checkOob(start, end) :
            if emptyOrOnePoint(i, True) == True :
                fromNowShouldEmpty = True;
                fromNowShouldEmptyStart = i + 1;
            break;
        if oneInLimit(i, start, end, True) :
            if i == 9 :
                AnswerArr.append((i, start));
                AnswerArr.append((i, end));
            start -= 1;
        elif emptyOrOnePoint(i, True) == True :
            AnswerArr.append((i - 1, start + 1));
            AnswerArr.append((i - 1, end));
            fromNowShouldEmpty = True;
            fromNowShouldEmptyStart = i + 1;
            break;
        else :
            isSatisfying = False;
            break;
if fromNowShouldEmpty :
    for i in range(fromNowShouldEmptyStart, 10) :
        if emptyOrOnePoint(i, True) != True :
            isSatisfying = False;
            break;
if checkIfOnlyOne() :
    isSatisfying = False;
if len(AnswerArr) != 3 :
    isSatisfying = False;
if isSatisfying :
    AnswerArr.sort();
    for e in AnswerArr :
        i, j = e;
        print(i + 1, j + 1);
    sys.exit();

#case3
AnswerArr = [];
isSatisfying = True;
sRow = -1; sCol = -1;
for i in range(9, -1, -1) :
    if i == 0 :
        isSatisfying = False;
    if emptyOrOnePoint(i, True) == True :
        continue;
    elif emptyOrOnePoint(i, True) == False :
        isSatisfying = False;
        break;
    else :
        sRow, sCol = emptyOrOnePoint(i, True);
        AnswerArr.append((sRow, sCol));
        break;
fromNowShouldEmpty = False;
fromNowShouldEmptyStart = -1;
if not (sRow == -1 and sCol == -1) :
    start = sCol;
    end = sCol + 1;
    for i in range(sRow - 1, -1, -1) :
        if not checkOob(start, end) :
            if emptyOrOnePoint(i, True) == True :
                fromNowShouldEmpty = True;
                fromNowShouldEmptyStart = i - 1;
            break;
        if oneInLimit(i, start, end, True) :
            if i == 0 :
                AnswerArr.append((i, start));
                AnswerArr.append((i, end));
            end += 1;
        elif emptyOrOnePoint(i, True) == True :
            AnswerArr.append((i + 1, start));
            AnswerArr.append((i + 1, end - 1));
            fromNowShouldEmpty = True;
            fromNowShouldEmptyStart = i - 1;
            break;
        else :
            isSatisfying = False;
            break;
if fromNowShouldEmpty :
    for i in range(fromNowShouldEmptyStart, -1, -1) :
        if emptyOrOnePoint(i, True) != True :
            isSatisfying = False;
            break;
if checkIfOnlyOne() :
    isSatisfying = False;
if len(AnswerArr) != 3 :
    isSatisfying = False;
if isSatisfying :
    AnswerArr.sort();
    for e in AnswerArr :
        i, j = e;
        print(i + 1, j + 1);
    sys.exit();

#case4
AnswerArr = [];
isSatisfying = True;
sRow = -1; sCol = -1;
for i in range(9, -1, -1) :
    if i == 0 :
        isSatisfying = False;
    if emptyOrOnePoint(i, True) == True :
        continue;
    elif emptyOrOnePoint(i, True) == False :
        isSatisfying = False;
        break;
    else :
        sRow, sCol = emptyOrOnePoint(i, True);
        AnswerArr.append((sRow, sCol));
        break;
fromNowShouldEmpty = False;
fromNowShouldEmptyStart = -1;
if not (sRow == -1 and sCol == -1) :
    start = sCol - 1;
    end = sCol;
    for i in range(sRow - 1, -1, -1) :
        if not checkOob(start, end) :
            if emptyOrOnePoint(i, True) == True :
                fromNowShouldEmpty = True;
                fromNowShouldEmptyStart = i - 1;
            break;
        if oneInLimit(i, start, end, True) :
            if i == 0 :
                AnswerArr.append((i, start));
                AnswerArr.append((i, end));
            start -= 1;
        elif emptyOrOnePoint(i, True) == True :
            AnswerArr.append((i + 1, start + 1));
            AnswerArr.append((i + 1, end));
            fromNowShouldEmpty = True;
            fromNowShouldEmptyStart = i - 1;
            break;
        else :
            isSatisfying = False;
            break;
if fromNowShouldEmpty :
    for i in range(fromNowShouldEmptyStart, -1, -1) :
        if emptyOrOnePoint(i, True) != True :
            isSatisfying = False;
            break;
if checkIfOnlyOne() :
    isSatisfying = False;
if len(AnswerArr) != 3 :
    isSatisfying = False;
if isSatisfying :
    AnswerArr.sort();
    for e in AnswerArr :
        i, j = e;
        print(i + 1, j + 1);
    sys.exit();

#case5
AnswerArr = [];
isSatisfying = True;
sRow = -1; sCol = -1;
for i in range(10) :
    if i == 9 :
        isSatisfying = False;
    if emptyOrOnePoint(i, True) == True :
        continue;
    elif emptyOrOnePoint(i, True) == False :
        isSatisfying = False;
        break;
    else :
        sRow, sCol = emptyOrOnePoint(i, True);
        AnswerArr.append((sRow, sCol));
        break;
fromNowShouldEmpty = False;
fromNowShouldEmptyStart = -1;
if not (sRow == -1 and sCol == -1) :
    start = sCol - 1;
    end = sCol + 1;
    for i in range(sRow + 1, 10) :
        if not checkOob(start, end) :
            if emptyOrOnePoint(i, True) == True :
                fromNowShouldEmpty = True;
                fromNowShouldEmptyStart = i + 1;
            break;
        if oneInLimit(i, start, end, True) :
            if i == 9 :
                AnswerArr.append((i, start));
                AnswerArr.append((i, end));
            end += 1;
            start -= 1;
        elif emptyOrOnePoint(i, True) == True :
            AnswerArr.append((i - 1, start + 1));
            AnswerArr.append((i - 1, end - 1));
            fromNowShouldEmpty = True;
            fromNowShouldEmptyStart = i + 1;
            break;
        else :
            isSatisfying = False;
            break;
if fromNowShouldEmpty :
    for i in range(fromNowShouldEmptyStart, 10) :
        if emptyOrOnePoint(i, True) != True :
            isSatisfying = False;
            break;
if checkIfOnlyOne() :
    isSatisfying = False;
if len(AnswerArr) != 3 :
    isSatisfying = False;
if isSatisfying :
    AnswerArr.sort();
    for e in AnswerArr :
        i, j = e;
        print(i + 1, j + 1);
    sys.exit();
#case6
AnswerArr = [];
isSatisfying = True;
sRow = -1; sCol = -1;
for i in range(9, -1, -1) :
    if i == 0 :
        isSatisfying = False;
    if emptyOrOnePoint(i, True) == True :
        continue;
    elif emptyOrOnePoint(i, True) == False :
        isSatisfying = False;
        break;
    else :
        sRow, sCol = emptyOrOnePoint(i, True);
        AnswerArr.append((sRow, sCol));
        break;
fromNowShouldEmpty = False;
fromNowShouldEmptyStart = -1;
if not (sRow == -1 and sCol == -1) :
    start = sCol - 1;
    end = sCol + 1;
    for i in range(sRow - 1, -1, -1) :
        if not checkOob(start, end) :
            if emptyOrOnePoint(i, True) == True :
                fromNowShouldEmpty = True;
                fromNowShouldEmptyStart = i - 1;
            break;
        if oneInLimit(i, start, end, True) :
            if i == 0 :
                AnswerArr.append((i, start));
                AnswerArr.append((i, end));
            start -= 1;
            end += 1;
        elif emptyOrOnePoint(i, True) == True :
            AnswerArr.append((i + 1, start + 1));
            AnswerArr.append((i + 1, end - 1));
            fromNowShouldEmpty = True;
            fromNowShouldEmptyStart = i - 1;
            break;
        else :
            isSatisfying = False;
            break;
if fromNowShouldEmpty :
    for i in range(fromNowShouldEmptyStart, -1, -1) :
        if emptyOrOnePoint(i, True) != True :
            isSatisfying = False;
            break;
if checkIfOnlyOne() :
    isSatisfying = False;
if len(AnswerArr) != 3 :
    isSatisfying = False;
if isSatisfying :
    AnswerArr.sort();
    for e in AnswerArr :
        i, j = e;
        print(i + 1, j + 1);
    sys.exit();

#case7
AnswerArr = [];
isSatisfying = True;
sRow = -1; sCol = -1;
for j in range(9, -1, -1) :
    if j == 0 :
        isSatisfying = False;
    if emptyOrOnePoint(j, False) == True :
        continue;
    elif emptyOrOnePoint(j, False) == False :
        isSatisfying = False;
        break;
    else :
        sRow, sCol = emptyOrOnePoint(j, False);
        AnswerArr.append((sRow, sCol));
        break;
fromNowShouldEmpty = False;
fromNowShouldEmptyStart = -1;
if not (sRow == -1 and sCol == -1) :
    start = sRow - 1;
    end = sRow + 1;
    for j in range(sCol - 1, -1, -1) :
        if not checkOob(start, end) :
            if emptyOrOnePoint(j, False) == True :
                fromNowShouldEmpty = True;
                fromNowShouldEmptyStart = j - 1;
            break;
        if oneInLimit(j, start, end, False) :
            if j == 0 :
                AnswerArr.append((start, j));
                AnswerArr.append((end, j));
            start -= 1;
            end += 1;
        elif emptyOrOnePoint(j, False) == True :
            AnswerArr.append((start + 1, j + 1));
            AnswerArr.append((end - 1, j + 1));
            fromNowShouldEmpty = True;
            fromNowShouldEmptyStart = j - 1;
            break;
        else :
            isSatisfying = False;
            break;
if fromNowShouldEmpty :
    for j in range(fromNowShouldEmptyStart, -1, -1) :
        if emptyOrOnePoint(j, False) != True :
            isSatisfying = False;
            break;
if checkIfOnlyOne() :
    isSatisfying = False;
if len(AnswerArr) != 3 :
    isSatisfying = False;
if isSatisfying :
    AnswerArr.sort();
    for e in AnswerArr :
        i, j = e;
        print(i + 1, j + 1);
    sys.exit();

#case8
AnswerArr = [];
isSatisfying = True;
sRow = -1; sCol = -1;
for j in range(10) :
    if j == 9 :
        isSatisfying = False;
    if emptyOrOnePoint(j, False) == True :
        continue;
    elif emptyOrOnePoint(j, False) == False :
        isSatisfying = False;
        break;
    else :
        sRow, sCol = emptyOrOnePoint(j, False);
        AnswerArr.append((sRow, sCol));
        break;
fromNowShouldEmpty = False;
fromNowShouldEmptyStart = -1;
if not (sRow == -1 and sCol == -1) :
    start = sRow - 1;
    end = sRow + 1;
    for j in range(sCol + 1, 10) :
        if not checkOob(start, end) :
            if emptyOrOnePoint(j, False) == True :
                fromNowShouldEmpty = True;
                fromNowShouldEmptyStart = j + 1;
            break;
        if oneInLimit(j, start, end, False) :
            if j == 9 :
                AnswerArr.append((start, j));
                AnswerArr.append((end, j));
            start -= 1;
            end += 1;
        elif emptyOrOnePoint(j, False) == True :
            AnswerArr.append((start + 1, j - 1));
            AnswerArr.append((end - 1, j - 1));
            fromNowShouldEmpty = True;
            fromNowShouldEmptyStart = j + 1;
            break;
        else :
            isSatisfying = False;
            break;
if fromNowShouldEmpty :
    for j in range(fromNowShouldEmptyStart, 10) :
        if emptyOrOnePoint(j, False) != True :
            isSatisfying = False;
            break;
if checkIfOnlyOne() :
    isSatisfying = False;
if len(AnswerArr) != 3 :
    isSatisfying = False;
if isSatisfying :
    AnswerArr.sort();
    for e in AnswerArr :
        i, j = e;
        print(i + 1, j + 1);
    sys.exit();

print(0);