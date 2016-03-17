import sys
import json

def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))

def main():
    afinnfile = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    scores = {} # initialize an empty dictionary
    for line in afinnfile:
        term, score  = line.split("\t")
        scores[term] = int(score)  # Convert the score to an integer.
	#print scores.items() # Print every (term, score) pair in the dictionary
    tweets = {}
    for line,val in enumerate (tweet_file):
        tweets[line] = json.loads(val)
        if "text" in tweets[line]:
            print(tweets[line]["text"])


if __name__ == '__main__':
    main()
