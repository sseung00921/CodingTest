import sys;
input = sys.stdin.readline;

mapper = {};
mapper["A"] = "000000"; mapper["B"] = "001111"; mapper["C"] = "010011"; mapper["D"] = "011100";
mapper["E"] = "100110"; mapper["F"] = "101001"; mapper["G"] = "110101"; mapper["H"] = "111010";

n = int(input());
strr = input();

def decider(inputSixLenStr, char) :
    targetSixLenStr = mapper[char];

    differCnt = 0;
    for i in range(6) :
        if inputSixLenStr[i] != targetSixLenStr[i] :
            differCnt += 1;

    if differCnt <= 1 :
        return True;

    return False

def parser(strr) :
    rtnTranslatedStr = '';
    for i in range(0, len(strr), 6) :
        if i + 6 > len(strr) :
            break;
        inputSixLenStr = strr[i : i + 6];
        if decider(inputSixLenStr, "A") == True : rtnTranslatedStr += "A"
        elif decider(inputSixLenStr, "B") == True : rtnTranslatedStr += "B"
        elif decider(inputSixLenStr, "C") == True : rtnTranslatedStr += "C"
        elif decider(inputSixLenStr, "D") == True : rtnTranslatedStr += "D"
        elif decider(inputSixLenStr, "E") == True : rtnTranslatedStr += "E"
        elif decider(inputSixLenStr, "F") == True : rtnTranslatedStr += "F"
        elif decider(inputSixLenStr, "G") == True : rtnTranslatedStr += "G"
        elif decider(inputSixLenStr, "H") == True : rtnTranslatedStr += "H"
        else :
            return (i // 6) + 1;
    return rtnTranslatedStr;

print(parser(strr));