import sys;
input = sys.stdin.readline;

N, D, K, C = map(int, input().split());
data = [];
for _ in range(N) :
    data.append(int(input()));

data = data[:] + data[:(K + 1)];

Sett = set();
Mapp = dict();
Mapp[C] = 1;
Sett.add(C);
MaxKind = -1;

for i in range(K) :
    if data[i] not in Mapp :
        Mapp[data[i]] = 1;
        Sett.add(data[i]);
    else :
        Mapp[data[i]] += 1;

MaxKind = max(MaxKind, len(Sett));

for i in range(1, N) :
    popedOutKind = data[i - 1];
    Mapp[popedOutKind] -= 1;
    if Mapp[popedOutKind] == 0 :
        Sett.remove(popedOutKind);
    newlyInKind = data[i + K - 1];
    if newlyInKind not in Mapp or Mapp[newlyInKind] == 0 :
        Mapp[newlyInKind] = 1;
        Sett.add(newlyInKind);
    else:
        Mapp[newlyInKind] += 1;
    MaxKind = max(MaxKind, len(Sett));

print(MaxKind);



