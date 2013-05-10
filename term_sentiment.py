import sys
import json
sentimentData = sys.argv[1] #AFINN-111.txt
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
    
    accum_term = dict()
    #Calculating sentiment scores for the whole tweet with unknown terms set to score of zero
    #then accumulate a dictionary of list of values with each new term occurance with the new term as key.
    for index in range(len(tweets)):
        if tweets[index].has_key("text"):
            tweet_word = tweets[index]["text"].split()
            sent_score = 0
            term_count = {}
            term_list = []
            
            for word in tweet_word:
                word = word.rstrip('?:!.,;"!@')
                word = word.replace("\n", "")
              
                if not (word.encode('utf-8', 'ignore') == ""):
                    if word.encode('utf-8') in sentiment.keys():
                        sent_score = sent_score + float(sentiment[word])
                        
                    else:
                        sent_score = sent_score
                        accum_term[word] = []
                        term_list.append(word)
                        if word.encode('utf-8') in term_count.keys():
                            term_count[word] = term_count[word] + 1
                        else:
                            term_count[word] = 1

          
            for word in term_list:
                accum_term[word].append(sent_score)
                
                        
                              

    for key in accum_term.keys():
        num_pos = 0
        num_neg = 0
        adjusted_score = 0
        term_value = 0
        total_sum = 0
        for score in accum_term[key]:
            total_sum = total_sum + score
            
                
        term_value = (total_sum)/len(accum_term[key])
        
        adjusted_score = "%.3f" %term_value
        print key.encode('utf-8') + " " + adjusted_score

        

        

if __name__ == '__main__':
    main()
