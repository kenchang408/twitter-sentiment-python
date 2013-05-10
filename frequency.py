import sys
import json

twitterData = sys.argv[1] #output.txt

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
   
    

def main():

    tweets = tweet_dict(twitterData)
    term_list = []
    total_list = {}#dict of term and corresponding # of occurance that term/ # of total terms
    punc_str = '?:!.,;"!@\''
    punc_chars_list = []
    for char in punc_str:
        punc_chars_list.append(char)
    #print punc_chars_list
    '''Create a method below that loops through each tweet in your 
    twees_list.  For each individual tweet it should add up you sentiment 
    score, based on the sent_dict.
    '''
    for index in range(len(tweets)):
        if tweets[index].has_key("text"):
            tweet_word = tweets[index]["text"].split()
            for word in tweet_word:
                word = word.rstrip(punc_str)
                #if not (word.encode("ASCII", "ignore")==''):
                    #get rid of all weird charcters and words with punctuation marks
                    #if not any(x in word.encode("ASCII", "ignore") for x in punc_chars_list): 
                term_list.append(word)# create list of total terms

    for word in term_list:
	if word in total_list:
		total_list[word] = total_list[word]+1
		
	else:
		total_list[word] = 1
		

    
    num_total = len(total_list)


    for word in total_list:
        total_list[word] = "%.3f" %(float(total_list[word])/num_total)
        print word.encode("utf-8") + " " + total_list[word]
		
	
       

        

        

if __name__ == '__main__':
    main()
