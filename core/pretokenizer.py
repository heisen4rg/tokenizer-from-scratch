from input_.txt2words import load_file
import string


def pretokenize(text):
    words = text.split()
    word_freq = {}
    for word in words:
        word = word.strip(string.punctuation) 
        if word not in word_freq:
            word_freq[word] = 1
        
        else:
            word_freq[word] += 1

    return word_freq



def char_split(word_freq):
    char_freq = {}
    for word in word_freq:
        chars = tuple(word)        
        char_freq[chars] = word_freq[word]   
    return char_freq