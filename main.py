import os
from input_.txt2words import load_file
from core.pretokenizer import pretokenize, char_split
from core.trainer import get_pair_count, merge_pair, train
from core.vocab import allocate_token_id, save_vocab


def question_1():
    while True:
        q1 = input("Do you want to tokenize content from a .txt file? (y/n): ")
        if q1 == 'y':
            return True
        elif q1 == 'n':
            print("okay! Have a nice day!")
            return False
        else:
            print("press either y or n only.")



def question_2():
    while True:
        path = input("Enter the file path of the .txt file: ")
        path = os.path.abspath(path)
        
        if not os.path.exists(path):
            print("File not found, please enter a valid path.")
        elif not path.endswith('.txt'):
            print("Only .txt files are supported.")
        else:
            print("File path info received successfully!")
            return path
    


def question_3():
    flag = True
    while flag:
        try:
            vocab = int(input("enter the size of your desired vocabulary in numerals only: "))
            if vocab <= 0:
                print("enter a valid number")
            else:
                return vocab
        except:
            print("enter a number")



def question_4():
    while True:
        path = input("Enter the folder path to save vocab and merges files (or press Enter for current directory): ")
        
        if path == "":
            return "./"
        
        path = os.path.abspath(path)
        
        if not os.path.exists(path):
            print("Folder not found, please enter a valid path.")
        else:
            return path + "/"




if __name__ == "__main__":

    print('''----------------------------
hello, welcome to tokenizer :D
----------------------------''')
    
    q1 = question_1()
    if q1:
        path = question_2()
        text = load_file(path)

        freq = pretokenize(text)
        print(f"Unique words: {len(freq)}")

        char_freq = char_split(freq)

        vocab_size = question_3()
        merges, final_char_freq = train(char_freq, vocab_size)

        print(f"\nTotal merges: {len(merges)}")
        print("\nMerge rules in order:")
        for i, pair in enumerate(merges):
            print(f"  merge {i+1}: {pair[0]} + {pair[1]} → {pair[0]+pair[1]}")
    
        first_10 = dict(list(final_char_freq.items())[:10])
        print(first_10)

        token_id = allocate_token_id(final_char_freq)

        print(f"Vocab size: {len(token_id)}")
        print("\nFirst 10 tokens:")
        for token, id in list(token_id.items())[:10]:
            print(f"  '{token}' → {id}")
    
        print("\nLast 10 tokens:")
        for token, id in list(token_id.items())[-10:]:
            print(f"  '{token}' → {id}")

        save_path = question_4()

        save_vocab(token_id, merges, save_path)
