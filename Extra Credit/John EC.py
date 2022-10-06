from string import punctuation

infile = open('book of John text.txt')
read = infile.read()
word_count = {}


words = read.split()

for word in words:
    if word in word_count:
        word_count[word] += 1

    else:
        word_count[word] = 1

wordlist = ['Spirit','Father','God','Christ','spirit','life','man']

for key in word_count:
    if key in wordlist:
        print(key + ': ' + str(word_count[key]))

   
infile.close()