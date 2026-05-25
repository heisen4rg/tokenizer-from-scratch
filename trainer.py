from pretokenizer import pretokenize, char_split
from txt2words import load_file



def get_pair_count(char_freq):
    pair_counts = {}
    for word, freq in char_freq.items():
        for j in range(len(word) - 1):
            pair = (word[j], word[j + 1])
            pair_counts[pair] = pair_counts.get(pair, 0) + freq
        
    return pair_counts



def merge_pair(pair, char_freq):
    new_char_freq = {}
    for word, freq in char_freq.items():
        i = 0
        new_word = []
        while i < len(word):
            if i < len(word) - 1 and word[i] == pair[0] and word[i + 1] == pair[1]:
                new_word.append(pair[0] + pair[1])
                i += 2
            else:
                new_word.append(word[i])
                i += 1
        new_char_freq[tuple(new_word)] = freq
    return new_char_freq



def train(char_freq, vocab_size):
    merge = []
    for i in range(vocab_size):
        pair_count = get_pair_count(char_freq)
        if not pair_count:
            break
        highest_freq_pair = max(pair_count, key=pair_count.get)
        merged_pair = merge_pair(highest_freq_pair, char_freq)
        char_freq = merged_pair
        merge.append(highest_freq_pair)
    
    return merge, char_freq



if __name__ == "__main__":
    text = load_file("/Users/heisen4rg/Downloads/shakespeare.txt")
    freq = pretokenize(text)
    char_freq = char_split(freq)
    
    merges, final_char_freq = train(char_freq, vocab_size=2000)
    
    print(f"\nTotal merges: {len(merges)}")
    print("\nMerge rules in order:")
    for i, pair in enumerate(merges):
       print(f"  merge {i+1}: {pair[0]} + {pair[1]} → {pair[0]+pair[1]}")
    
    first_10 = dict(list(final_char_freq.items())[:10])
    print(first_10)
