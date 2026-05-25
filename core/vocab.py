from txt2words import load_file
from pretokenizer import pretokenize, char_split
from trainer import train
import json



def allocate_token_id(final_char_freq):
    token = set()
    for word_tuple in final_char_freq:
        for t in word_tuple:
            token.add(t)

    dummy_list = list(token)
    dummy_list.sort(key=len)

    token_id = {}
    for i, char in enumerate(dummy_list):
        token_id[char] = i

    return token_id



def save_vocab(vocab, merges, path="./"):

    with open(path + "vocab.json", "w", encoding="utf-8") as f:
        json.dump(vocab, f, ensure_ascii=False, indent=2)
    
    merges_serializable = [list(pair) for pair in merges]
    with open(path + "merges.json", "w", encoding="utf-8") as f:
        json.dump(merges_serializable, f, ensure_ascii=False, indent=2)
    
    print(f"saved vocab.json ({len(vocab)} tokens)")
    print(f"saved merges.json ({len(merges)} merges)")



if __name__ == "__main__":
    text = load_file("/Users/heisen4rg/Downloads/shakespeare.txt")
    freq = pretokenize(text)
    char_freq = char_split(freq)
    
    merges, final_char_freq = train(char_freq, vocab_size=2000)
    
    vocab = allocate_token_id(final_char_freq)
    
    print(f"Vocab size: {len(vocab)}")
    print("\nFirst 10 tokens:")
    for token, id in list(vocab.items())[:10]:
        print(f"  '{token}' → {id}")
    
    print("\nLast 10 tokens:")
    for token, id in list(vocab.items())[-10:]:
        print(f"  '{token}' → {id}")
    
    save_vocab(vocab, merges)