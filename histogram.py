import argparse
from collections import defaultdict


def buckets_histogram(nums, w, o, init_empty_buckets=True):
    '''Calculates the number of elements for each bucket

    Given a list of nums, a window size and an overlap range, this method
    calculates how many numbers will fall to each bucket.
    First bucket starts at 0 and has window size. Next ones have also window
    size but they start at the next position of the last pos of the previous
    bucket minus the overlap size. So multiple buckets can have the same number
    due to overlap.
    The bucket ID is a range but can be expressed with it's first num, for
    example with:
    window: 10
    overlap: 2
    bucket 1 with ID "0-9" and bucket 2 with ID "8-17" can be expressed like:
    bucket1: 0, bucket2: 8 because we know the window.

    So the return of this method is a dict where each key is the first position
    of the bucket and the value is the number of times a number will fall in.

    By default this method first initializes each bucket empty for the given
    values but we can pass the argument init_empty_buckets=False and populate
    only those buckets with numbers in them.
    '''
    buckets = defaultdict(int)
    b_dist = w - o
    max_num = nums[-1]
    if init_empty_buckets:
        for i in range(0, max_num + 1, b_dist):
            buckets[i] = 0
    for n in nums:
        last_b_id = n // b_dist
        first_b_n = last_b_id * b_dist
        buckets[first_b_n] += 1
        while True:  # check overlap backwards
            first_b_n -= b_dist
            last_b_n = first_b_n + w - 1
            if last_b_n >= n and first_b_n >= 0:
                buckets[first_b_n] += 1
            else:
                break
    return dict(buckets)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-n', '--nums', nargs='+', type=int, required=True)
    parser.add_argument('-w', '--window', type=int, required=True)
    parser.add_argument('-o', '--overlap', type=int, required=True)
    args = parser.parse_args()
    buckets = buckets_histogram(args.nums, args.window, args.overlap)
    print(buckets)
