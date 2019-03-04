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
    parser.add_argument('--prefix', type=str, help='file prefix(write)', required=True)
    args = parser.parse_args()

    prefix  = args.prefix
    num_fd  = 100
    fd_list = []
    for i in range(num_fd):
        fd = open(prefix + '.%s'%i, 'w')
        fd_list.append(fd)

    bucket_count = 0
    bucket = []
    while 1:
        try: line = sys.stdin.readline()
        except KeyboardInterrupt: break
        if not line: break
        line = line.strip()
        if not line and len(bucket) >= 1:
            idx = random.randint(0, num_fd-1)
            fd = fd_list[idx]
            sys.stderr.write('[bucket_count] : %s' % bucket_count + '\n')
            spill(fd, bucket)
            bucket = []
            bucket_count += 1
        if line : bucket.append(line)
    if len(bucket) != 0:
        idx = random.randint(0, num_fd-1)
        fd = fd_list[idx]
        spill(fd, bucket)
    
    for i in range(num_fd):
        fd_list[i].close()
