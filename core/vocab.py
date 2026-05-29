from input_.txt2words import load_file
from core.pretokenizer import pretokenize, char_split
from core.trainer import train
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