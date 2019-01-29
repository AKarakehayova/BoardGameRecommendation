from textblob import TextBlob
import json
with open('./ForumCrawler/comments.json') as comments:
        comment = json.load(comments)
        i = 0
        strComments=''
        while i < len(comment):
            stringified = json.dumps(comment[i])
            strComments += stringified
            i+=1
        tb = TextBlob(strComments)
        f = open("test.json", "a")
f.write(str(tb.correct()))
