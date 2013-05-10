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
        #twitter_list_dict.append(json.loads(line.decode('utf-8-sig')))
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
    state_dict = dict()
    
    
    
    
    
    '''Create a method below that loops through each tweet in your 
    twees_list.  For each individual tweet it should add up you sentiment 
    score, based on the sent_dict.
    '''
    for index in range(len(tweets)):
        if all(k in tweets[index].keys() for k in ("text","place")):
            if not (tweets[index]["place"] == None):
                #if not (type(tweets[index]["place"]["state_code"]) == "NoneType"):
                    tweet_word = tweets[index]["text"].split()
                    tweet_state = tweets[index]["place"]["country_code"]
                    sent_score = 0
                    for word in tweet_word:
            
                        if word.encode('utf-8') in sentiment.keys():
                            sent_score = sent_score + float(sentiment[word])
                        else:
                            sent_score = sent_score

                    if tweet_state.encode('utf-8') in state_dict.keys():
                        state_dict[tweet_state].append(sent_score)
                    else:
                        state_dict[tweet_state] = []
                        state_dict[tweet_state].append(sent_score)

    state_list = []                        
    max_score = 0
    happiest_state = ""
    for state in state_dict.keys():
        state_score = 0
        state_list = state_dict[state]
   
        for score in state_list :
            state_score = state_score + float(score)
        
        state_score = state_score/len(state)
                              
        if happiest_state == "" or state_score > max_score:
            max_score = state_score
            happiest_state = state
          
    
        

        
    
    print happiest_state
                    
    





    
if __name__ == '__main__':
    main()
