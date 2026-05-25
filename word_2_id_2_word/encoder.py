import json
import string



def load_vocab(path="./data/"):
    with open(path + "vocab.json", "r", encoding="utf-8") as f:
        vocab = json.load(f)
    
    with open(path + "merges.json", "r", encoding="utf-8") as f:
        merges_list = json.load(f)

    merges = []
    for pair in merges_list:
        merges.append(tuple(pair))
    
    return vocab, merges



def encode(text, vocab, merges):
    words = text.split()

    cleaned_words = []
    for word in words:
        w = word.strip(string.punctuation)
        if w != "":
            cleaned_words.append(w)

    char_words = []
    for word in cleaned_words:
        char_words.append(tuple(word))

    token_ids = []
    for word in char_words:
        for pair in merges:
            new_word = []
            i = 0
            while i < len(word):
                if i < len(word)-1 and word[i] == pair[0] and word[i+1] == pair[1]:
                    new_word.append(pair[0] + pair[1])
                    i += 2
                else:
                    new_word.append(word[i])
                    i += 1
            word = tuple(new_word)
        
        for token in word:
            token_ids.append(vocab[token])
    
    return token_ids

if __name__ == "__main__":
    vocab, merges = load_vocab()

    text = "to be or not to be"
    ids = encode(text, vocab, merges)
    
    print(f"text: {text}")
    print(f"token ids: {ids}")
    print(f"number of tokens: {len(ids)}")