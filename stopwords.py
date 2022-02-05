# from nltk.corpus import stopwords
# nltk.download('stopwords')
# from nltk.tokenize import word_tokenize
#fileName = "D:\sample.txt";
# file = open(fileName);
# with open('D:\sample.txt','r') as file:
#     wordstring = file.read()
# print(wordstring);
#
# text = wordstring
# text_tokens = word_tokenize(text)
#
# tokens_without_sw = [word for word in text_tokens if not word in stopwords.words()]
#
# print(tokens_without_sw)

import re
fileName = "D:\sample.txt";
file = open(fileName);
with open('D:\sample.txt','r') as file:
    wordstring = file.read()
print("The article is : " + wordstring)
wordstring = re.sub("[^\w\s]", "", wordstring)
wordlist = wordstring.split()
print("The list of words in the article is : ")
print(wordlist)



stopwords = ["a", "about", "above", "after", "again", "against", "all", "am", "an", "and", "any", "are", "aren't",
             "as", "at", "be", "because", "been", "before", "being", "below", "between", "both", "but", "by", "can't",
             "cannot", "could", "couldn't", "did", "didn't", "do", "does", "doesn't", "doing", "don't", "down",
             "during", "each", "few", "for", "from", "further", "had", "hadn't", "has", "hasn't", "have", "haven't",
             "having", "he", "he'd", "he'll", "he's", "her", "here", "here's", "hers", "herself", "him", "himself",
             "his", "how", "how's", "I", "I'd", "I'll", "I'm", "I've", "if", "in", "into", "is", "isn't", "it", "it's",
             "its", "itself", "let's", "me", "more", "most", "mustn't", "my", "myself", "nor", "nor", "not", "of",
             "off", "on", "once", "only", "or", "other", "ought", "our", "ours", "ourselves", "out", "over", "own",
             "same", "shan't", "she", "she'd", "she'll", "she's", "should", "shouldn't", "so", "some", "such", "than",
             "that", "that's", "the", "their", "theirs", "them", "themselves", "then", "there", "there's", "these",
             "they", "they'd", "they'll", "they're", "they've", "this", "those", "through", "to", "too", "under",
             "until", "up", "very", "was", "wasn't", "we", "we'd", "we'll", "we're", "we've", "were", "weren't", "what",
             "what's", "when", "when's", "where", "where's", "which", "while", "who", "who's", "whom", "why", "why's",
             "with", "won't", "would", "wouldn't", "you", "you'd", "you'll", "you're", "you've", "your", "yours",
             "yourself", "yourselves"];

for words in wordlist:
    for word in stopwords:
        if(words.lower() == word.lower()):
            wordlist.remove(words)
print("\nThe list of words in the article after stopwords are removed : ")
print(wordlist)

# Gdex
# gdexfileName = "D:\gdex.txt";
# gdexfile = open(gdexfileName);
# with open('D:\gdex.txt','r') as file:
#     gdexwordstring = gdexfile.read()
# print("The article is : " + gdexwordstring)
# gdexwordstring = re.sub("[^\w\s]", "", gdexwordstring)
# gdexwordlist = gdexwordstring.split()
# print("The list of words in the article is : ")
# print(gdexwordlist)

