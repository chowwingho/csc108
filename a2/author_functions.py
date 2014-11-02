# need to figure out how to properly split sentences into phrases and account 
# for internal punctuation. 



##########  Provided helper function. ############

def clean_up(s):
    """ (str) -> str

    Return a new string based on s in which all letters have been
    converted to lowercase and punctuation characters have been stripped 
    from both ends. Inner punctuation is left untouched. 

    >>> clean_up('Happy Birthday!!!')
    'happy birthday'
    >>> clean_up("-> It's on your left-hand side.")
    " it's on your left-hand side"
    """
    
    punctuation = """!"',;:.-?)([]<>*#\n\t\r"""
    result = s.lower().strip(punctuation)
    return result


##########  Complete the following functions. ############

def avg_word_length(text):
    """ (list of str) -> float

    Precondition: text is non-empty. Each str in text ends with \n and
    text contains at least one word.

    Return the average length of all words in text. 
    
    >>> avg_word_length(['apple pear!\n'])
    4.5
    >>> avg_word_length(['apple\n', 'orange\n'])
    5.5
    """
    
    text = wordify_list(text)
  
    for i in range(len(text)):
        text[i] =  len(text[i])
        
    return sum(text) / len(text)

def type_token_ratio(text):
    """ (list of str) -> float

    Precondition: text is non-empty. Each str in text ends with \n and
    text contains at least one word.

    Return the Type Token Ratio (TTR) for this text. TTR is the number of
    different words divided by the total number of words.
    
    >>>type_token_ratio(['apple'])
    1.0
    >>>type_token_ratio(['apple', 'apple', 'banana, pear\n'])
    0.75
    """
    words = wordify_list(text)
    unique_words = uniqueify_list(words)
    
    return len(unique_words) / len(words)
                
def hapax_legomena_ratio(text):
    """ (list of str) -> float

    Precondition: text is non-empty. Each str in text ends with \n and
    text contains at least one word.

    Return the hapax legomena ratio for text. This ratio is the number of 
    words that occur exactly once divided by the total number of words.
    
    >>> hapax_legomena_ratio(['apple'])
    1.0
    >>> hapax_legomena_ratio(['apple', 'apple', 'banana, pear\n'])
    0.5
    """
   
    words = wordify_list(text)
    strict_unique_words = strict_uniqueify_list(words)
    
    return len(strict_unique_words) / len(words)    


def split_on_separators(original, separators):
    """ (str, str) -> list of str

    Return a list of non-empty, non-blank strings from original,
    determined by splitting original on any of the separators.
    separators is a string of single-character separators.

    >>> split_on_separators("Hooray! Finally, we're done.", "!,")
    ['Hooray', ' Finally', " we're done."]
    """
    
    if original == "":
        return []
    
    result = [original]
    for sep in separators:
        for i in range(len(result)):
            result[i] = result[i].split(sep)
        result = [item for sublist in result for item in sublist]
    return [item for item in result if (item != "" and not item.isspace())]          
    
def avg_sentence_length(text):
    """ (list of str) -> float

    Precondition: text contains at least one sentence.
    
    A sentence is defined as a non-empty string of non-terminating 
    punctuation surrounded by terminating punctuation or beginning or 
    end of file. Terminating punctuation is defined as !?.

    Return the average number of words per sentence in text.   

    >>> text = ['The time has come, the Walrus said\n',
         'To talk of many things: of shoes - and ships - and sealing wax,\n',
         'Of cabbages; and kings.\n',
         'And why the sea is boiling hot;\n',
         'and whether pigs have wings.\n']
    >>> avg_sentence_length(text)
    17.5    
    
    
    
    >>> avg_sentence_length(['The apple is good.'])
    4.0
    >>> avg_sentence_length(['The apple is good.', 'I like apples, pears, \ 
    and bananas!\n'])
    5.0
    """
        
    for i in range(len(text)):
        text[i] = text[i].strip()
    
    file_as_str = ' '.join(text)
    sentences = split_on_separators(file_as_str, '!?.')
    words = wordify_list(sentences)
    
    return len(words) / len(sentences)
    

def avg_sentence_complexity(text):
    """ (list of str) -> float

    Precondition: text contains at least one sentence.    

    A sentence is defined as a non-empty string of non-terminating
    punctuation surrounded by terminating punctuation or beginning or
    end of file. Terminating punctuation is defined as !?.
    Phrases are substrings of sentences, separated by one or more of ,;:

    Return the average number of phrases per sentence in text.

    >>> text = ['The time has come, the Walrus said\n',
         'To talk of many things: of shoes - and ships - and sealing wax,\n',
         'Of cabbages; and kings.\n',
         'And why the sea is boiling hot;\n',
         'and whether pigs have wings.\n']
    >>> avg_sentence_complexity(text)
    3.5
    """
    
    # To do: Fill in this function's body to meet its specification.
    # same as above, only once each sentence is split from the text, split it
    # further into the number of phrases in each sentence, rather than the 
    # number of words. Then generate a second list that is made of numbers 
    # corresponding to the number of phrases in each sentence in the previous
    # list. Then find the average of those numbers. 
    
    
def compare_signatures(sig1, sig2, weight):
    """ (list, list, list of float) -> float

    Return a non-negative float indicating the similarity of the two 
    linguistic signatures, sig1 and sig2. The smaller the number the more
    similar the signatures. Zero indicates identical signatures.
    
    sig1 and sig2 are 6-item lists with the following items:
    0  : Author Name (a string)
    1  : Average Word Length (float)
    2  : Type Token Ratio (float)
    3  : Hapax Legomena Ratio (float)
    4  : Average Sentence Length (float)
    5  : Average Sentence Complexity (float)

    weight is a list of multiplicative weights to apply to each
    linguistic feature. weight[0] is ignored.

    >>> sig1 = ["a_string" , 4.4, 0.1, 0.05, 10.0, 2.0]
    >>> sig2 = ["a_string2", 4.3, 0.1, 0.04, 16.0, 4.0]
    >>> weight = [0, 11.0, 33.0, 50.0, 0.4, 4.0]
    >>> compare_signatures(sig1, sig2, weight)
    12.000000000000007
    """
    
    # To do: Fill in this function's body to meet its specification.
    
    # need to see what the math is for this question - doesn't seem too 
    # logically difficult 
  
  ################# Helper Functions #################
  
  
    
def flatten_list(l):
    """ (list) -> list
    
    Return a flattened list
    
    >>> flatten_list([])
    []
    >>> flatten_list(['a', 'b'])
    ['a', 'b']
    >>> flatten_list(['a', ['b', ['c']]])
    ['a', 'b', ['c']]
    """
    return [item for sublist in l for item in sublist]

def uniqueify_list(l):
    ''' 
    (list) -> list
    
    Return a list containing only unique items found in the given list.
    
    >>> uniqueify_list([]) 
    []
    >>> uniqueify_list(['a', 'a', 'b', 'c'])
    ['a', 'b', 'c']
    '''   
    
    seen = set()
    unique_list = []
    
    for item in l:
        if item not in seen:
            unique_list.append(item)
            seen.add(item)
    return unique_list

def wordify_list(l):
    '''
    (list) -> list
    
    Return a list of words from a list of strings
    
    >>> wordify_list([])
    []
    >>> wordify_list(['a', 'b, c\n'])
    ['a', 'b', 'c']
    '''
    
    words = []
    for i in range(len(l)):
        words.append(l[i].split())
        
    words = flatten_list(words) 
    for i in range(len(words)):
        words[i] = clean_up(words[i])
    
    return words

def strict_uniqueify_list(l):
    '''
    (list) -> list
    
    Return a list of items that occur only once in l.
    >>> strict_uniqueify_list(['apple'])
    ['apple']
    >>> strict_uniqueify_list(['apple', 'apple', 'banana', 'pear'])
    ['banana', 'pear']
    '''
    seen = set()
    strict_unique_list = []
     
    for item in l:
        if item not in seen:
            strict_unique_list.append(item)
            seen.add(item)
        elif item in strict_unique_list:
            strict_unique_list.remove(item)
    
    return strict_unique_list   
    

if __name__ == '__main__':
    # tests for flatten_list
    assert flatten_list([]) == []
    assert flatten_list(['a', 'b']) == ['a', 'b']
    assert flatten_list(['a', ['b', ['c']]]) == ['a', 'b', ['c']]
    
    # tests for avg_word_length
    assert avg_word_length(['apple pear!\n']) == 4.5
    assert avg_word_length(['apple\n', 'orange\n']) == 5.5
    
    # tests for split_on_separators
    assert split_on_separators("", "!?.") == []
    assert split_on_separators("apple", "") == ["apple"]
    assert split_on_separators("apple, pear", "!") == ["apple, pear"]
    assert split_on_separators("apple, pear!! orange?", "!,") == \
           ['apple', ' pear', " orange?"]
    
    # tests for uniqueify_list
    assert uniqueify_list([]) == []
    assert uniqueify_list(['a', 'a', 'b', 'c']) == ['a', 'b', 'c']
    
    # tests for wordify_list
    assert wordify_list([]) == []
    assert wordify_list(['a', 'b, c\n']) == ['a', 'b', 'c']    
    
    # tests for type_token_ratio
    assert type_token_ratio(['apple']) == 1.0
    assert type_token_ratio(['apple', 'apple', 'banana, pear\n']) == 0.75
    
    # tests for strict_uniqueify_list   
    assert strict_uniqueify_list(['apple']) == ['apple']
    assert strict_uniqueify_list(['apple', 'apple', 'banana', 'pear']) == \
           ['banana', 'pear']  
    
    # tests for hapax_legomena_ratio
    assert hapax_legomena_ratio(['apple']) == 1.0
    assert hapax_legomena_ratio(['apple', 'apple', 'banana, pear\n']) == 0.5 

    # tests for avg_sentence_length
    assert avg_sentence_length(['The apple is good.']) == 4.0
    assert avg_sentence_length(['The apple is good.', 'I like apples, ' + \
                                'pears, and bananas!\n']) == 5.0    
