from txt2words import load_file
import string



def pretokenize(text):
    words = text.split()
    freq = {}
    for word in words:
        word = word.strip(string.punctuation) 
        if word not in freq:
            freq[word] = 1
        
        else:
            freq[word] += 1

    return freq



def char_split(freq):
    char_freq = {}
    for word in freq:
        chars = tuple(word)        
        char_freq[chars] = freq[word]   
    return char_freq
            


if __name__ == "__main__":
    text = load_file("/Users/heisen4rg/Downloads/shakespeare.txt")
    freq = pretokenize(text)
    print(f"Unique words: {len(freq)}")
    print(sorted(freq.items(), key=lambda x: x[1], reverse=True)[:10])
    char_freq = char_split(freq)
    for k, v in list(char_freq.items())[:5]:
        print(k, "→", v)