from textblob import TextBlob
import glob
import json

files = glob.glob('./SearchEngine/*.txt')
classification = open("classification.json", "w")
games = []
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
        gameName = gameName.replace(".txt", "")
        newLine = {
            'name': gameName,
            'count': counter,
            'polarity': polarity/counter,
            'subjectivity': subjectivity/counter
        }
        games.append(newLine)

classification.write(json.dumps(games))