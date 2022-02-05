# modules
from bs4 import BeautifulSoup
import requests
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

nltk.download('punkt')
nltk.download('stopwords')

# imports for scatter plots
# import numpy as np
# import plotly
# import plotly.graph_objects as go
# import plotly.offline as pyo
# from plotly.offline import init_notebook_mode


def main():
    urls = [
        # citylink
        [
            'https://www.truckandbusnews.net/latest-news/posts/2018/november/city-link-express-aims-for-fast-delivery-and-customer-satisfaction-with-isuzu/',
            'https://themalaysianreserve.com/2020/05/28/courier-service-a-lifeline-in-time-of-enforced-isolation/',
            'https://www.theedgemarkets.com/article/crossing-borders-and-boundaries',
        ],
        [
            # poslaju
            'https://themalaysianreserve.com/2020/06/09/delivery-firms-focus-on-efficient-operations/',
            'https://www.theborneopost.com/2020/07/08/poslaju-customers-urged-to-bear-with-longer-waiting-time/',
            'https://soyacincau.com/2020/08/15/pos-malaysia-e-consignment-notes-qr-code-available/',
        ],
        [
            # gdex
            'https://www.thestar.com.my/business/business-news/2020/05/30/brisk-business-for-gdex',
            'https://www.thestar.com.my/business/business-news/2021/01/30/digitalisation-a-game-changer-for-gdex',
            'https://www.thestar.com.my/news/nation/2021/01/29/couriers-and-postmen-should-also-get-vaccination-priority',
        ],
        [
            # J&T
            'https://www.malaymail.com/news/malaysia/2021/02/07/courier-company-jt-express-explains-staffs-violent-handling-of-parcels-caug/1947791',
            'https://www.thestar.com.my/news/nation/2019/11/10/jt-express-anticipates-promising-1111-big-sale',
            'https://hype.my/2021/212126/jt-express-courier-truck-has-only-a-few-items-to-deliver-following-bad-publicity/',
        ],
        # DHL
        [
            'https://www.trackingmore.com/review-dhl.html',
            'https://www.trustpilot.com/review/dhl-express.de',
            'https://www.asiaone.com/business/dhl-ecommerce-integrated-shopee-offering-malaysians-nextday-delivery-service',
        ]
    ]

    # rabin karp function
    # def rabinkarpsearch(pat, txt, q):
    #     M = len(pat)
    #     N = len(txt)
    #     i = 0
    #     j = 0
    #     keyword = 0
    #     text = 0
    #     hvalue = 1
    #     global found
    #     found = 0
    #
    #     for i in range(M - 1):
    #         hvalue = (hvalue * 10) % q
    #     for i in range(M):
    #         keyword = (10 * keyword + ord(pat[i])) % q
    #         text = (10 * text + ord(txt[i])) % q
    #     for i in range(N - M + 1):
    #         if keyword == text:
    #             for j in range(M):
    #                 if txt[i + j] != pat[j]:
    #                     break
    #                 else:
    #                     j += 1
    #             if j == M:
    #                 found = 1
    #                 # print ("Pattern found at index " + str(i))
    #                 break
    #         if i < N - M:
    #             text = (10 * (text - ord(txt[i]) * hvalue) + ord(txt[i + M])) % q
    #             if text < 0:
    #                 text = text + q

    #Boyer Moore function with Good Suffix heuristic
    def strong_suffix(shift, bpos, pat, m):
        i = m
        j = m + 1
        bpos[i] = j

        while i > 0:
            while j <= m and pat[i - 1] != pat[j - 1]:
                if shift[j] == 0:
                    shift[j] = j - i
                j = bpos[j]
            i -= 1
            j -= 1
            bpos[i] = j

    def preprocess_case2(shift, bpos, pat, m):
        j = bpos[0]
        for i in range(m + 1):
            if shift[i] == 0:
                shift[i] = j
            if i == j:
                j = bpos[j]

    def search(text, pat):
        s = 0
        m = len(pat)
        n = len(text)
        global found
        found = 0
        bpos = [0] * (m + 1)
        shift = [0] * (m + 1)
        strong_suffix(shift, bpos, pat, m)
        preprocess_case2(shift, bpos, pat, m)

        while s <= n - m:
            j = m - 1
            while j >= 0 and pat[j] == text[s + j]:
                j -= 1
            if j < 0:
                found = 1
                break
                s += shift[0]
            else:
                s += shift[j + 1]

    # Boyer Moore function with Bad Character heuristic
    # NO_OF_CHARS = 257
    # def badCharHeuristic(string, size):
    #     badChar = [-1] * NO_OF_CHARS
    #     for i in range(size):
    #         badChar[ord(string[i])] = i;
    #     return badChar
    #
    # def search(txt, pat):
    #     m = len(pat)
    #     n = len(txt)
    #     global found
    #     found = 0
    #
    #     badChar = badCharHeuristic(pat, m)
    #     s = 0
    #     while (s <= n - m):
    #         j = m - 1
    #         while j >= 0 and pat[j] == txt[s + j]:
    #             j -= 1
    #         if j < 0:
    #             found = 1
    #             # print("Pattern occur at shift = {}".format(s))
    #             break
    #             s += (m - badChar[ord(txt[s + m])] if s + m < n else 1)
    #         else:
    #             s += max(1, j - badChar[ord(txt[s + j])])

    # Test each word
    def testword(pat, count):
        positive = open("D:/positive.txt", "r", encoding='utf-8')
        negative = open("D:/negative.txt", "r", encoding='utf-8')
        # q = 131
        global cpositive, cnegative, cneutral
        search(positive.read(), pat)
        if found == 1:
            count[0] += 1
        else:
            search(negative.read(), pat)
            if found == 1:
                count[1] += 1
            else:
                count[2] += 1

    def remove(string):
        string = string.replace("'", "")
        string = string.replace(".", " ")
        string = string.replace("(", "")
        string = string.replace(")", "")
        string = string.replace("%", "")
        string = string.replace(",", " ")
        string = string.replace("\"", "")
        string = string.lower()
        return string

    def scrape(link):
        r = requests.get(link)
        soup = BeautifulSoup(r.content, 'lxml')
        news = soup.find_all('p')

        newsstring = ''

        # get text form for each line and add it into newsstring, remove symbols etc
        for string in news:
            s = str(string.get_text())
            newsstring += remove(s)

        # delete stopwords and updated text without stopwords
        tokenized_newsstring = word_tokenize(newsstring)
        # newsstring_without_sw = [word for word in tokenized_newsstring if not word in stopwords.words()]

        stringlist = tokenized_newsstring
        for i in stringlist:
            search(stopwords.words(), i)
            if found == 1:
                stringlist.remove(i)

        newsstring_without_sw = stringlist


        # filtered newsstring free from stopwords
        filtered_newsstring = newsstring_without_sw

        # get frequency of every word
        newslist = filtered_newsstring

        # empty array for putting frequency of each word
        newsfreq = []
        for word in newslist:
            newsfreq.append(newslist.count(word))

        # print each word and its respective frequencies in each article
        print("Pairs\n" + str(list(zip(newslist, newsfreq))))

        # scatter plots for every link
        # fig = go.Figure(data=go.Scatter(x=newslist, y=newsfreq, mode='markers'))
        # fig.show()

        pw = list()
        nw = list()

        # Drive Code
        # count array is for number of +ve, -ve and neutral words. count[0] is for +ve, count[1] is for -ve, count[2] is
        # for neutral
        count = [0, 0, 0]
        for i in newslist:
            testword(i, count)
            pw.append(count[0])
            nw.append(count[1])

        print(count)

    # loop for every url in urls
    for courier in urls:
        for url in courier:
            scrape(url)
            print('--------------------------------------------------------')


if __name__ == '__main__':
    main()



