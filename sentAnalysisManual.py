from textblob import TextBlob
from textblob.classifiers import NaiveBayesClassifier
import glob
import json

files = glob.glob('./SearchEngine/*.txt')
classification = open("classification2.json", "w")
games = []


with open('test.csv', 'r') as fp: 
    cl = NaiveBayesClassifier(fp, format="csv")


for file in files:
    with open(file) as f:
        lines = [line.rstrip('\n') for line in f]
        polarity = 0
        subjectivity = 0
        counter = 0
        
        for line in lines:
            tb = TextBlob(line, classifier=cl)
            prob_dist = cl.prob_classify(tb)
            posProb = round(prob_dist.prob("pos"), 2)
            polarity = polarity + posProb
            counter = counter + 1 

        gameName = file.replace("./SearchEngine/", "")
        gameName = gameName.replace(".txt", "") #todo regex 
        newLine = {
            'name': gameName,
            'count': counter,
            'polarity': polarity/counter
        }    
     
        games.append(newLine)

classification.write(json.dumps(games))