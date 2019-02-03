from textblob import TextBlob
import glob

files = glob.glob('./SearchEngine/*.txt')
print(files)
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
        print(file)
        print(polarity/counter)
        print(subjectivity/counter)
        print('----------------')



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