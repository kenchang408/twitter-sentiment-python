import sys
import json
sentimentData = sys.argv[1] #AFIN-111.txt
twitterData = sys.argv[2] #output.txt

def tweet_dict(twitterData):  
    ''' (file) -> list of dictionaries
    This method should take your output.txt
    file and create a list of dictionaries.
    '''
    twitter_list_dict = []
    twitterfile = open(twitterData)
    for line in twitterfile:
        twitter_list_dict.append(json.loads(line))
    return twitter_list_dict
    #return data_read["text"]
    
def sentiment_dict(sentimentData):
    ''' (file) -> dictionary
    This method should take your sentiment file
    and create a dictionary in the form {word: value}
    '''
    afinnfile = open(sentimentData)
    scores = {} # initialize an empty dictionary
    for line in afinnfile:
        term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
        scores[term] = float(score)  # Convert the score to an integer.

    return scores # Print every (term, score) pair in the dictionary


def main():

    tweets = tweet_dict(twitterData)
    sentiment = sentiment_dict(sentimentData)
    

    '''Create a method below that loops through each tweet in your 
    twees_list.  For each individual tweet it should add up you sentiment 
    score, based on the sent_dict.
    '''
    for index in range(len(tweets)):
        if tweets[index].has_key("text"):
            tweet_word = tweets[index]["text"].split()
            sent_score = 0
            new_term = {}
            for word in tweet_word:
                word = word.rstrip('?:!.,;"!@')
                #
                word.replace("\n", " ")
                if word.encode('utf-8', "ignore") in sentiment.keys():
                    sent_score = sent_score + float(sentiment[word])
                else:
                    sent_score = sent_score
                    new_term[word] = 0
        
        #print all the new term and assign the corresponding tweet score to all the new terms in the tweet
            for term in new_term:
                new_term[term] = float(sent_score)
                print "%s %.3f"%(term.encode('utf-8'), new_term[term])

        

        

if __name__ == '__main__':
    main()
