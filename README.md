# eng-tokenizer

A Byte Pair Encoding (BPE) tokenizer built from scratch in Python, 
designed for English language corpora.

## What it does
Learns a vocabulary from a `.txt` corpus using the BPE algorithm — 
the same technique used by GPT-2, GPT-4, and other large language models.

## Files
- `txt2words.py` — loads and cleans a .txt file
- `pretokenizer.py` — splits text into words and characters with frequencies
- `trainer.py` — runs the BPE merge loop to learn vocabulary

## Usage
Provide any English `.txt` file and a target vocab size.
The trainer outputs ordered merge rules that form the tokenizer vocabulary.

## Status
Work in progress — encoder and decoder coming next.