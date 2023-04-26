m = dict();

def checkIfFired(nowDate, signedDate, monthByTerm) :
    nowYear, nowMonth, nowDay = nowDate.split('.');
    now = int(nowYear)*28*12 + int(nowMonth)*28 + int(nowDay);
    signedYear, signedMonth, signedDay = signedDate.split('.');
    signed = int(signedYear)*28*12 + int(signedMonth)*28 + int(signedDay);

    return now - signed >= 28*monthByTerm;

def solution(today, terms, privacies):
    for term in terms :
        name, month = term.split();
        m[name] = month;

    answer = [];
    for i in range(len(privacies)) :
        signedDate, term = privacies[i].split();
        if checkIfFired(today, signedDate, int(m[term])) :
            answer.append(i + 1);
    return answer

today = "2022.05.19"
terms = ["A 6", "B 12", "C 3"];
privacies = ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"];
print(solution(today, terms, privacies));