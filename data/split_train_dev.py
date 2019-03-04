from __future__ import print_function
import sys
import argparse
import random

def spill(fd, bucket):
    for line in bucket:
        fd.write(line + '\n')
    fd.write('\n')

if __name__ == '__main__':
    
    parser = argparse.ArgumentParser()
    parser.add_argument('--dev', type=str, help='dev data(write)', required=True)
    args = parser.parse_args()

    dev_path = args.dev
    dev_fd = open(dev_path, 'w')

    bucket = []
    while 1:
        try: line = sys.stdin.readline()
        except KeyboardInterrupt: break
        if not line: break
        line = line.strip()
        if not line and len(bucket) >= 1:
            fd = dev_fd
            if random.randint(0, 1000): fd = sys.stdout
            spill(fd, bucket)
            bucket = []
        if line : bucket.append(line)
    if len(bucket) != 0:
        fd = dev_fd
        if random.randint(0, 1000): fd = sys.stdout
        spill(fd, bucket)
    
    dev_fd.close()
