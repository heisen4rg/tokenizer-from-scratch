from txt2words import load_file
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
            


if __name__ == "__main__":
    text = load_file("/Users/heisen4rg/Downloads/shakespeare.txt")
    freq = pretokenize(text)
    print(f"Unique words: {len(freq)}")
    print(sorted(freq.items(), key=lambda x: x[1], reverse=True)[:10])
    char_freq = char_split(freq)
    for k, v in list(char_freq.items())[:5]:
        print(k, "→", v)