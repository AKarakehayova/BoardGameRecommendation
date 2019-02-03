from textblob import TextBlob
import glob

files = glob.glob('./SearchEngine/*.txt')
# print(files)
classification = open("classification.txt", "a")
for file in files:
    with open(file) as f:
        lines = [line.rstrip('\n') for line in f]
        polarity = 0
        subjectivity = 0
        counter = 0
        for line in lines:
            tb = TextBlob(line)
            polarity = polarity + tb.sentiment.polarity
            subjectivity = subjectivity + tb.sentiment.subjectivity
            counter = counter + 1
        gameName = file.replace("./SearchEngine/", "")
        gameName = gameName.replace(".txt", "") #todo regex 
        newLine = "" + gameName + "---" + str(polarity/counter) + "---" + str(subjectivity/counter) + "\n" 
        classification.write(newLine)





# print(tb.sentiment)

# print(t.sentiment)
# for sentence in tb.sentences:
    # print(sentence.sentiment)



# file=open("./SearchEngine/kemet.txt")
# t=file.read()
# tb = TextBlob(t)
# print(tb.sentiment)

# with open("./SearchEngine/kemet.txt") as f:
#     lines = [line.rstrip('\n') for line in f]

# polarity = 0
# subjectivity = 0
# counter = 0
# for line in lines:
#     tb = TextBlob(line)
#     polarity = polarity + tb.sentiment.polarity
#     subjectivity = subjectivity + tb.sentiment.subjectivity
#     counter = counter + 1