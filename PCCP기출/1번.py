Duration = 0;
HealPerSec = 0;
BonusHeal = 0;
Health = 0;
MaxHealth = 0;
def heal(givenTime) :
    global Health;
    bonusCnt = (givenTime - 1) // Duration;
    Health = min(MaxHealth, Health + (HealPerSec * (givenTime - 1)) + (BonusHeal * bonusCnt))

def solution(bandage, health, attacks):
    global Duration; global HealPerSec; global BonusHeal; global Health; global MaxHealth;
    Duration, HealPerSec, BonusHeal = bandage;
    Health = health;
    MaxHealth = health;
    nowTime = 0;
    for a in attacks :
        time, deal = a;
        givenTime = time - nowTime;
        nowTime = time;
        heal(givenTime);
        Health -= deal;
        if Health <= 0 :
            return -1;

    return Health;

bandage = [3, 2, 7];
health = 20;
attacks = [[1, 15], [5, 16], [8, 6]]
print(solution(bandage, health, attacks));