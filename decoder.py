import json



def load_vocab(path="./"):
    with open(path + "vocab.json", "r", encoding="utf-8") as f:
        vocab = json.load(f)
    return vocab



def decode(token_ids, vocab):
    reversed_vocab = {}
    for chars, id in vocab.items():
        reversed_vocab[id] = chars
    
    tokens = []
    for token in token_ids:
        tokens.append(reversed_vocab[token])
    
    output_string = "".join(tokens)
    return output_string



if __name__ == "__main__":
    vocab = load_vocab()
    
    token_ids = [191, 172, 113, 364, 191, 172]
    decoded = decode(token_ids, vocab)
    
    print(f"token ids: {token_ids}")
    print(f"decoded text: {decoded}")