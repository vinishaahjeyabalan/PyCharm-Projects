def KMPSearch(pat, txt):
    M = len(pat)  # length of pattern
    N = len(txt)  # length of text
    lps = [0] * M  # create empty lps array same size as pattern
    j = 0  # pointer for pattern
    i = 0  # pointer for text
    computeLPSArray(pat, M, lps)  # execute the function to compute lps
    while i < N:
        # if letter at both index match, increment both i and j
        if pat[j] == txt[i]:
            i += 1
            j += 1

        if j == M:  # if j reached the end of pattern
            # print("Found pattern at index " + str(i - j))
            # j = lps[j - 1]

        # if letter at both index mismatch
        # elif i < N and pat[j] != txt[i]:
        #     if j != 0:
        #         j = lps[j - 1]
        #     else:  # if j is already 0, we cant go back. So, increment i
        #         i += 1


def computeLPSArray(pat, M, lps):
    # initialize two pointers len and i for pattern
    len = 0  # pointer len starts at 1st index
    i = 1  # pointer i starts at 2nd index
    lps[0] = 0
    while i < M:
        if pat[i] == pat[len]:
            len += 1
            lps[i] = len
            i += 1
        else:
            if len != 0:
                len = lps[len - 1]
            else:  # when letter at index i and len mismatch, set lps[i] to 0 and increment i by 1
                lps[i] = 0
                i += 1


stopwords = ["a", "about", "above", "after", "again", "against", "all", "an", "am", "and", "any", "are", "aren't",
             "as", "at", "be", "because", "been", "before", "being", "below", "between", "both", "but", "by", "can't",
             "cannot", "could", "couldn't", "did", "didn't", "do", "does", "doesn't", "doing", "don't", "down",
             "during", "each", "few", "for", "from", "further", "had", "hadn't", "has", "hasn't", "have", "haven't",
             "having", "he", "he'd", "he'll", "he's", "her", "here", "here's", "hers", "herself", "him", "himself",
             "his", "how", "how's", "i", "i'd", "i'll", "i'm", "i've", "if", "in", "into", "is", "isn't", "it", "it's",
             "its", "itself", "let's", "me", "more", "most", "mustn't", "my", "myself", "nor", "nor", "not", "of",
             "off", "on", "once", "only", "or", "other", "ought", "our", "ours", "ourselves", "out", "over", "own",
             "same", "shan't", "she", "she'd", "she'll", "she's", "should", "shouldn't", "so", "some", "such", "than",
             "that", "that's", "the", "their", "theirs", "them", "themselves", "then", "there", "there's", "these",
             "they", "they'd", "they'll", "they're", "they've", "this", "those", "through", "to", "too", "under",
             "until", "up", "very", "was", "wasn't", "we", "we'd", "we'll", "we're", "we've", "were", "weren't", "what",
             "what's", "when", "when's", "where", "where's", "which", "while", "who", "who's", "whom", "why", "why's",
             "with", "won't", "would", "wouldn't", "you", "you'd", "you'll", "you're", "you've", "your", "yours",
             "yourself", "yourselves"];

for word in stopwords:
    if word in file:
        print(word)
