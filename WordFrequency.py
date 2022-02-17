#Read the contents of the AI.txt file 
infile = open("AI.txt", "r")

words = infile.read()
words = words.lower()

#Group the characters to be removed and replace with whitespace
special_char = [',', '!', '.', '@', '#', ':', ';', '?', '(', ')', '-', '"']
special_char = str(special_char)

for index in special_char:
    words = words.replace(index, ' ')
words = words.split()

#Create a list to track word count 
wordlist = []

for key in words:
    wordlist.append(key)

#Create a dictionary for the individual words 
wordfreq = {}

#Initialize or increase counter if word is present in the dictionary 
for word in words:
    if word in wordfreq:
        counter = wordlist.count(word)
        wordfreq[word] = counter
    else:
        wordfreq[word] = 1 

#Display word count for each individual word 
for key in list(wordfreq.keys()):
    print(key, ": ", wordfreq[key], sep = '')