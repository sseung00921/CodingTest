tc = int(input());

while tc > 0 :
    member = input();
    fan = input();
    memberSize = len(member);
    fanSize = len(fan);
    memberBin = int(member.replace('M', '1').replace('F', '0'), 2);
    fanBin = int(fan.replace('M', '1').replace('F', '0'), 2);

    cnt = 0;
    for i in range(fanSize - memberSize + 1) :
        if memberBin & fanBin == 0 :
            cnt += 1;
        memberBin <<= 1;
    print(cnt);
    tc -= 1;