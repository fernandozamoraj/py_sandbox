import unittest

MIN_SCORE = .7
g_words = []

def print1(line):
    pass
    #print(line);
    
def is_possible_replacement(target_word, possible_word):
    global MIN_SCORE
	
    score = 0
	
    print1('*'*40)
  
    if(target_word[0] == possible_word[0]):
        score += 100
    if(target_word[-1] == possible_word[-1]):
        score += 100

    first_set = {x for x in target_word[1:-1]}
    second_set = {x for x in possible_word[1:-1]}

    intersection_set = first_set.intersection(second_set)
	
    if(len(second_set) > len(first_set)):
        longer_set = len(second_set)
    else:
        longer_set = len(first_set)
	
    score_for_matching_chars = ((len(intersection_set)*100.0) / (longer_set*100.0))*.75
    
    score_first_and_last_chars = ((score*1.0)/(200.0))*.25
    demerit = 0
    if(len(possible_word) > len(target_word)):
        diff = len(possible_word) - len(target_word)
        demerit = (diff/(len(possible_word)*1.0))*.5		
    else:
        diff = len(target_word) - len(possible_word)
        demerit = (diff/(len(target_word)*1.0))*.5
	
    total_score = (score_for_matching_chars + score_first_and_last_chars) - demerit;
	
    return total_score > MIN_SCORE
	
def get_words(target_word):
    global g_words

    if(len(g_words) < 1):    
        file = open('C:/Dev/python/py_sandbox/words.txt')
        g_words = file.read().split('\n')
    filtered_words = []   
        
    for word in g_words:        
        if(len(word) > 0 and word[0] == target_word[0]):
            print1(word)
            filtered_words.append(word)
            
    return filtered_words
    
def correct_word(target_word):
    for word in get_words(target_word):
        if(is_possible_replacement(target_word, word)):
            return word 
def is_word(target_word):
    for word in get_words(target_word):
        if(word == target_word):
            return True
            
    return False
            
def prompt():
    
    while(True):
        print('\nEntere a word: \n');
        user_entry = input();
        new_word = user_entry
        
        if(is_word(user_entry) == False):
            new_word = correct_word(user_entry)
     
        print('Your corrected word is: {0}'.format(new_word))
        if(new_word == 'quit'):
            break;        
	

class test_auto_correct(unittest.TestCase):

    def test_check_exact_word(self):
        itis = is_possible_replacement('automobile', 'automobile')
		
        self.assertTrue(itis)		

    def test_check_possible_word(self):
        itis = is_possible_replacement('automobile', 'automobile')
		
        self.assertTrue(itis)		
	
    def test_check_aardvark_word(self):
        itis = is_possible_replacement('ark', 'aardvark')
		
        self.assertFalse(itis)		
		
    def test_check_ark_word(self):
        itis = is_possible_replacement('aardvark', 'ark')
		
        self.assertFalse(itis)			

    def test_check_apple_people(self):
        itis = is_possible_replacement('apple', 'people')
		
        self.assertFalse(itis)		
		
    def test_check_spaghetti_spageti(self):
        itis = is_possible_replacement('spageti', 'spaghetti')
		
        self.assertTrue(itis)	

    def test_check_sapgetti(self):
        itis = is_possible_replacement('sapgetti', 'spaghetti')
		
        self.assertTrue(itis)			

    def test_check_acomodate(self):
        itis = is_possible_replacement('acomodate', 'accommodate')
		
        self.assertTrue(itis)
		
    def test_check_acomodat(self):
        itis = is_possible_replacement('acomodat', 'accommodate')
		
        self.assertTrue(itis)	

    def test_check_acknolegement(self):
        itis = is_possible_replacement('acknolegment', 'acknowledgement')
		
        self.assertTrue(itis)	

    def test_check_typo(self):
        itis = is_possible_replacement('assird', 'assure')
		
        self.assertTrue(itis)			
	
if(__name__ == '__main__'):
    #unittest.main()
    #get_words('foo') 
    prompt()    
	
