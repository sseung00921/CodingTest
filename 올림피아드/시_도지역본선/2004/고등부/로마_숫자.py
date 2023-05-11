m1 = dict(); m2 = dict(); m3 = dict(); m4 = dict();
m1[0] = ""; m1[1] = "M"; m1[2] = "MM"; m1[3] = "MMM";
m2[0] = ""; m2[1] = "C"; m2[2] = "CC"; m2[3] = "CCC"; m2[4] = "CD"; m2[5] = "D"; m2[6] = "DC"; m2[7] = "DCC"; m2[8] = "DCCC"; m2[9] = "CM";
m3[0] = ""; m3[1] = "X"; m3[2] = "XX"; m3[3] = "XXX"; m3[4] = "XL"; m3[5] = "L"; m3[6] = "LX"; m3[7] = "LXX"; m3[8] = "LXXX"; m3[9] = "XC";
m4[0] = ""; m4[1] = "I"; m4[2] = "II"; m4[3] = "III"; m4[4] = "IV"; m4[5] = "V"; m4[6] = "VI"; m4[7] = "VII"; m4[8] = "VIII"; m4[9] = "IX";
RomaToNum = dict();

def numToRoma(num) :
    rtnStr = "";

    temp = num // 1000;
    rtnStr += m1[temp];
    num -= temp*1000;

    temp = num // 100;
    rtnStr += m2[temp];
    num -= temp*100;

    temp = num // 10;
    rtnStr += m3[temp];
    num -= temp*10;

    rtnStr += m4[num];

    return rtnStr;

for i in range(0, 4000) :
    RomaToNum[numToRoma(i)] = i;

a = input();
b = input();
numA = RomaToNum[a];
numB = RomaToNum[b];

print(numA + numB);
print(numToRoma(numA + numB));