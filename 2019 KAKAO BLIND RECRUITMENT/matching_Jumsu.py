class Page :
    def __init__(self, idx, basic, outterLinkCnt, matchingScore) :
        self.idx = idx;
        self.basic = basic;
        self.outterLinkCnt = outterLinkCnt;
        self.matchingScore = matchingScore;

    def __lt__(self, other) :
        if self.matchingScore == other.matchingScore :
            return self.idx < other.idx;
        return self.matchingScore > other.matchingScore;

def solution(word, pages) :
    word = word.lower();
    wSize = len(word);
    urlHash = dict();
    pageList = [];
    for i, s in enumerate(pages) :
        s = s.lower();
        mid = -1;
        posl = -1; posr = 0;
        while mid < 0 :
            posl = s.find("<meta", posl + 1);
            posr = s.find(">", posl);
            mid = s.find("https://", posl, posr);
            if mid != -1 :
                posr = s.find("\"", mid);
                url = s[mid : posr];
                urlHash[url] = i;

        basic = 0;
        posl = -1;
        while True :
            posl = s.find(word, posl + 1);
            if posl != -1 :
                if not s[posl - 1].isalpha() and not s[posl + wSize].isalpha() :
                    basic += 1;
                    posl += wSize;
            else :
                break;

        outterLinkCnt = 0;
        posl = -1; posr = 0;
        while True :
            posl = s.find("<a", posl + 1);
            if posl == -1 :
                break;
            outterLinkCnt += 1;

        pageList.append(Page(i, basic, outterLinkCnt, basic));

    for i, s in enumerate(pages) :
        posl = -1; posr = 0;
        while True :
            posl = s.find("<a", posl + 1);
            if posl == -1 :
                break;
            else :
                posl = s.find("https://", posl);
                posr = s.find("\"", posl);
                outterLinkUrl = s[posl : posr];
                if outterLinkUrl in urlHash :
                    idx = urlHash[outterLinkUrl];
                    pageList[idx].matchingScore += pageList[i].basic/pageList[i].outterLinkCnt;

    pageList.sort();

    return pageList[0].idx;

word = "blind";
pages = ["<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://a.com\"/>\n</head>  \n<body>\nBlind Lorem Blind ipsum dolor Blind test sit amet, consectetur adipiscing elit. \n<a href=\"https://b.com\"> Link to b </a>\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://b.com\"/>\n</head>  \n<body>\nSuspendisse potenti. Vivamus venenatis tellus non turpis bibendum, \n<a href=\"https://a.com\"> Link to a </a>\nblind sed congue urna varius. Suspendisse feugiat nisl ligula, quis malesuada felis hendrerit ut.\n<a href=\"https://c.com\"> Link to c </a>\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://c.com\"/>\n</head>  \n<body>\nUt condimentum urna at felis sodales rutrum. Sed dapibus cursus diam, non interdum nulla tempor nec. Phasellus rutrum enim at orci consectetu blind\n<a href=\"https://a.com\"> Link to a </a>\n</body>\n</html>"];
print(solution(word, pages));