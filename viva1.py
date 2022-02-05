# lps is the longest prefix that is also suffix
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
            print("Found pattern at index " + str(i - j))
            j = lps[j - 1]

        # if letter at both index mismatch
        elif i < N and pat[j] != txt[i]:
            if j != 0:
                j = lps[j - 1]
            else:  # if j is already 0, we cant go back. So, increment i
                i += 1


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


txt = "Algorithmisfun"
pat = "fun"
KMPSearch(pat, txt)


''''# lps is longest prefix that is also suffix
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
            print("Found pattern at index " + str(i - j))
            j = lps[j - 1]

        # if letter at both index mismatch
        elif i < N and pat[j] != txt[i]:
            if j != 0:
                j = lps[j - 1]
            else:  # if j is already 0, we cant go back. So, increment i 
                i += 1


def computeLPSArray(pat, M, lps):
    # initializa two pointers len and i for pattern
    len = 0  # pointer len starts at 1st index
    i = 1  # pointer i starts at 2nd index
    lps[0]
    while i < M:
        if pat[i] == pat[len]:
            len += 1
            lps[i] = len
            i += 1
        else:
            if len != 0:
                len = lps[len - 1]
            else:  # when letter at index i and len mismatch, set lps[i] to 0 and increment i
                lps[i] = 0
                i += 1


txt = "Algorithmisfunghfun"
pat = "fun"
KMPSearch(pat, txt)'''