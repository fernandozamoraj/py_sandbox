# This is not my code.. rather it belongs to the person at the following link
# norvig.com/spell-correct.html
# for the record as of 4/17/2016 I have not been able to get this code to work
# I don't what may be wrong with it. I copied it manually from the link above so
# I might have copied something incorrectly


import re, collections

def words(text): return re.findall('[a-z]+', text.lower())

def train(features):
    model = collections.defaultdict(lambda: 1)
    for f in features:
       model[f] += 1
    return model

NWORDS = train(words(open('big.txt').read()))

alphabet = 'abcdefghijklmnopqrstuvwxyz'

def edits1(word):
    splits     = [(word[:i], word[i:]) for i in range(len(word) + 1)]
    deletes    = [a + b[1:] for a, b in splits if b]
    transposes = [a + b[1] + b[0] +b[2:] for a, b in splits if len(b)>1]
    replaces   = [a + c + b[1:] for a, b in splits for c in alphabet]
    inserts    = [a + c + b     for a, b in splits for c in alphabet]
    return set(deletes + transposes + replaces + inserts)

def known_edits2(word):
    global NWORDS
    return set(e2 for e1 in edits1(word) for e2 in edits1(e1) if e2 in NWORDS)

def known(words):
    global NWORDS
    if(words is None):
        return set()
    else:
        return set(w for w in words if w in NWORDS)

def correct(word):
    global NWORDS
    candidates = known([word]) or known(edits1(word)) or known_edits2(word) or [word]
	
    #get all words that start with same first letter... it is unlikely that
    #a speller does not know what character a word starts with
    #this change made by Fernando from original
    newcandidates = [w for w in candidates if word[0] == w[0]]
	
    #if(len(newcandidates) > 0):
    #    return max(newcandidates, key=NWORDS.get)
    #else:
    return max(candidates, key=NWORDS.get)
		
def prompt_stupid_autocorrect():
    while(True):
        print('\nEnter your message: ') 
        user_entry = input().split(' ')
        new_sentence = ''
        for word in user_entry:	
            correction = correct(word)
            new_sentence = new_sentence + correction + ' '
        
        print(new_sentence)
    
    

def prompt():
    while(True):
        print('\nEnter a word: ') 
        user_entry = input()
        correction = correct(user_entry)
        print(correction)


if(__name__ == '__main__'):
    prompt_stupid_autocorrect()
 
