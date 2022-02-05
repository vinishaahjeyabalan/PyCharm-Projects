# from urllib.request import urlopen as uReq
# from bs4
# fileName = input("Enter the filename: ");
# fileName = "D:\sample.txt";
# try:
#     file = open(fileName)
#     d1 = dict()
#     for line in file:
#         words = line.split("\n")
#         for word in words:
#             if word in d1:
#                 d1[word] = d1[word] + 1
#             else:
#                 d1[word] = 1
#     print(d1)
# except:
#     print("File not found")

import re
print("Poslaju Article\n")
fileName = "D:\sampletext.txt";
file = open(fileName);
with open('D:\sampletext.txt','r') as file:
    wordstring = file.read()
# print(wordstring);

punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
wordstring_nopunct = ""
for char in wordstring:
   if char not in punctuations:
       wordstring_nopunct = wordstring_nopunct + char

# print(wordstring_nopunct)
wordstring = wordstring_nopunct
wordstring = re.sub("[^\w\s]", "", wordstring)
wordlist = wordstring.split()
wordfreq = []
for w in wordlist:
    wordfreq.append(wordlist.count(w))
# print("String\n" + wordstring +"\n")
print("List of words in article :\n" + str(wordlist) + "\n")
print("Frequencies of words in article :\n" + str(wordfreq) + "\n")
print("Pairs :\n" + str(list(zip(wordlist, wordfreq))))


# GDEX
print("\nGdex Article\n")
gdexfileName = "D:\gdex.txt";
gdexfile = open(gdexfileName);
with open('D:\gdex.txt','r') as file:
    gdexwordstring = gdexfile.read()
# print(wordstring);

# punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
gdexwordstring_nopunct = ""
for char in gdexwordstring:
   if char not in punctuations:
       gdexwordstring_nopunct = gdexwordstring_nopunct + char

# print(wordstring_nopunct)
gdexwordstring = gdexwordstring_nopunct
gdexwordstring = re.sub("[^\w\s]", "", gdexwordstring)
gdexwordlist = gdexwordstring.split()
gdexwordfreq = []
for w in gdexwordlist:
    gdexwordfreq.append(gdexwordlist.count(w))
# print("String\n" + wordstring +"\n")
print("List of words in article :\n" + str(gdexwordlist) + "\n")
print("Frequencies of words in article :\n" + str(gdexwordfreq) + "\n")
print("Pairs :\n" + str(list(zip(gdexwordlist, gdexwordfreq))))






































# file = open("C:\Users\Vinishaah Jeyabalan\PycharmProjects\plotly", 'w')
# file.write("Hi Vinishaah here"
# content = file.read()
# print(content)





