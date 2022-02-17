#Read the contents of the AI.txt file 
infile = open("AI.txt", "r")

words = infile.readline()
words = words.lower()

special_char = [',', '!', '.', '@', '#', ':', ';', '?', '(', ')', '-', '"']
special_char = str(special_char)

#Create dictionary for the individual words 
wordfreq = {}

for x in special_char:
    words = words.replace(x, ' ')
words = words.split()
words = words.lower()

wordlist = []

for key in words:
    wordlist.append(key)

for word in words:
    if word in wordfreq:
        counter = wordlist.count(word)
        wordfreq[word] = counter
    else:
        wordfreq[word] = 1 

for key in list(wordfreq.keys()):
    print(key, ": ", wordfreq[key], sep = '')