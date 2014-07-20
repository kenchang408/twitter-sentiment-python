#!/usr/bin/python
import sys
import json

sentimentData = sys.argv[1] #AFIN-111.txt
twitterData = sys.argv[2] #output.txt

def tweet_dict(twitterData):  
  
    twitter_list_dict = []
    twitterfile = open(twitterData)
    for line in twitterfile:
       twitter_list_dict.append(json.loads(line)) 
    return twitter_list_dict
    
    
def sentiment_dict(sentimentData):
   
    afinnfile = open(sentimentData)
    scores = {} 
    for line in afinnfile:
        term, score  = line.split("\t")  
        scores[term] = int(score)  

    return scores 
    
def main():
    tweets = tweet_dict(twitterData)
    sentiment = sentiment_dict(sentimentData)
    for index in range(len(tweets)):
        if index and 'text' in tweets[index]:
            tweet_word = tweets[index]['text'].split()
            sent_score = 0
            for word in tweet_word:
                word = word.rstrip('?:!.,;"!@')
                word = word.replace("\n", "")
            
                if not (word.encode('utf-8', 'ignore') == ""):
                    if word.encode('utf-8') in sentiment.keys():
                        sent_score = sent_score + float(sentiment[word])
                    
                    else:
                        sent_score = sent_score

            print float(sent_score)
  
if __name__ == '__main__':
    main()
