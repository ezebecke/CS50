import nltk

class Analyzer():
    """Implements sentiment analysis."""

    def __init__(self, positives, negatives):
        #function to load positives and negatives words
        """Initialize Analyzer."""
        #we want to load de positives and negatives word in some struct that allows us tracking and search it.
        #options are list, dict or set. then store the words in self.positives or self.negatives
        #omite withspaces and  with str.strip function
        #str.startwith to not include lines with ;

        self.negatives = []
        with open("negative-words.txt") as file:
            for line in file:
                if line.startswith((';')) == False:
                    line = line.strip()
                    self.negatives.append(line)

        self.positives = []
        with open("positive-words.txt") as file:
            for line in file:
                #if line.startswith("\n") == True:
                    #print('hola')
                if line.startswith((';')) == False:
                    line = line.strip()
                    self.positives.append(line)

        #print('', self.negatives[1997])
        #print('', self.positives)


    def analyze(self, text):
        """Analyze text for sentiment, returning its score."""
        #analize every word in the text a value -1, 1 or 0 and calculate total score
        #tokens allow us to split words in single tokens we can initialize tokens like this:

        tokenizer = nltk.tokenize.TweetTokenizer()
        tokens = tokenizer.tokenize(text.lower())

        score = 0

        if tokens[0] in self.negatives:
            score =- 1
        elif tokens[0] in self.positives:
            score =+ 1
        else:
            score = 0

        #print('', text)

        return score


