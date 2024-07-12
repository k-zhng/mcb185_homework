import gzip
import sys
import math

def stats():
    gffpath = sys.argv[1]
    feature = sys.argv[2]
    lengths = []
    with gzip.open(gffpath, 'rt') as fp:
        for line in fp:
            if (line[0] != '#'):
                words = line.split()
                if (words[2] == feature):
                    beg = int(words[3])
                    end = int(words[4])
                    lengths.append(end - beg + 1)

    count = len(lengths)
    min_length = sys.maxsize
    max_length = -1 * sys.maxsize
    total = 0
    for num in lengths:
        total += num
        if (num < min_length):
            min_length = num
        if (num > max_length):
            max_length = num
    mean = total / count
    std = 0
    for num in lengths:
        std += (num - mean) ** 2
    std = math.sqrt(std / (count))
    median = lengths[1]
    lengths.sort()
    if (count % 2 == 0):
        median = (lengths[int(count/2)] + lengths[int(count/2) - 1]) / 2
    else:
        median = lengths[count/2]
    return (count, min_length, max_length, mean, std, median)
print(stats())