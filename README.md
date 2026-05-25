# tokenizer-from-scratch

A Byte Pair Encoding (BPE) tokenizer built from scratch in Python, 
designed for English language corpora.

The current version of this (v1.0.0) only works on corpuses of the English language using character splitting when a whitespace is occurred and merging rules.

Further development will allow to work on different languages where there are no whitespaces, using byte level breakdown of the text instead of character splitting.

## What it does

Learns a vocabulary from a `.txt` corpus using the BPE algorithm — 
the same technique used by GPT-2 and other large language models.

## How it works

The English text from the .txt file is broken down by first splitting the words every time a whitespace is encountered and counting the frequency of each unique word, then storing them as key:value pair in a dictionary.

The words from the above dictionary keys are then split into single chars and stored as a tuple:frequency in a new dictionary

Like {"the":7281, ..} --> {('t', 'h', 'e'):7281, ..}

Then, the tuple dictionary is iterated over counting every adjacent pair of characters weighted by their word frequency.

The most frequent pair is merged into a single token on every word in the dictionary simultaneously across every word in the corpus.

This process repeats until the target vocabulary size is reached. Each merge rule is recorded in order.

merge 1: t + h → th
merge 2: th + e → the

The final output is two files saved to disk:
- vocab.json  → every unique token mapped to an ID number
                Like 'the' : 452, 'ing' : 82
- merges.json → the ordered list of merge rules

These two files ARE the trained tokenizer. Any new 
English text can then be encoded into token IDs using 
the merge rules, and decoded back to text using the 
vocabulary.

## Usage

## Pipeline

Corpus (input .txt file) --> pretokenize --> char split --> BPE merges --> vocab --> encode/decode

## Files
- `txt2words.py` — loads and cleans a .txt file
- `pretokenizer.py` — splits text into words and characters with frequencies
- `trainer.py` — runs the BPE merge loop to learn vocabulary
- `vocab.py` - creates token IDs for every unique tokens that the BPE algorithm produced. Also creates the merge rules and token ID JSON files for the input .txt file.
- `encoder.py/decoder.py` - encodes words to token IDs and decodes token IDs back to words with the help of data from the JSON files.

## Status
Work in progress — Planning to turn it from character level to byte level tokenizer 

## Version History
v1.0.0 - English only, character level BPE (Current ver)