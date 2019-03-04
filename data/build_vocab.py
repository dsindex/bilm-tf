from __future__ import print_function
import sys
import argparse

if __name__ == '__main__':
    
    parser = argparse.ArgumentParser()
    args = parser.parse_args()

    vocab = {}
    while 1:
        try: line = sys.stdin.readline()
        except KeyboardInterrupt: break
        if not line: break
        line = line.strip()
        if not line: continue
        tokens = line.split()
        for token in tokens:
            if token in vocab:
                vocab[token] += 1
            else:
                vocab[token] = 1

    vocab_list = sorted(vocab.items(), key=lambda x: x[1], reverse=True)
    for token, freq in vocab_list:
        if freq < 10: continue
        print(token)
