scoreBoard = dict();
scoreBoard["A"] = 0; scoreBoard["C"] = 0; scoreBoard["M"] = 0; scoreBoard["R"] = 0;
scoreBoard["N"] = 0; scoreBoard["F"] = 0; scoreBoard["J"] = 0; scoreBoard["T"] = 0;

def coverTheChoice(kind, score) :
    north = kind[0];
    south = kind[1];
    if score <= 3 :
        scoreBoard[north] += (4 - score);
    elif score >= 5 :
        scoreBoard[south] += (score - 4);
def solution(survey, choices):
    for i in range(len(survey)) :
        coverTheChoice(survey[i], choices[i]);

    answer = ''
    if scoreBoard["R"] >= scoreBoard["T"] :
        answer += "R";
    else:
        answer += "T"
    if scoreBoard["C"] >= scoreBoard["F"] :
        answer += "C";
    else:
        answer += "F"
    if scoreBoard["J"] >= scoreBoard["M"] :
        answer += "J";
    else:
        answer += "M"
    if scoreBoard["A"] >= scoreBoard["N"] :
        answer += "A";
    else:
        answer += "N"
    return answer

survey = ["AN", "CF", "MJ", "RT", "NA"];
choices = [5, 3, 2, 7, 5];
print(solution(survey, choices));