# Histogram Buckets

## The exercise is:

Give these parameters:
- numbers: List[int]    example: [1, 4, 5, 10, 20, 35]
- window: int           example: 1
- overlap: int          example 0

Calculate "buckets" and how many times one of these numbers "fall" in one of these buckets.

A bucket is a range of numbers, the first bucket starts at 0 and contains "window" numbers, if window is 1, then it only contains [0], if window is 10 then [0-9].
Next bucket starts at the next position of the last position of the previous bucket, for example with a window of 10, first bucket ends at 9 and second bucket starts at 10.
And overlap defines a shift of the starting position of each new bucket. If second bucket should start at 10 but we have an overlap of 1, it will start at 9. The first bucket is not affected by overlap

For example: with window 1 and overlap 0, we will have buckets like:
[0], [1], [2], [3], etc
if window is 10, overlap 0:
[0-9], [10-19], [20-29], etc.

When we have overlap of 1, is the same but the next bucket starts with 1 less position:
with window 2 and overlap 1:
[0-1], [1-2], [2-3], [3-4], etc
with window 10 and overlap 1:
[0-9], [9-18], [18-27], [27-36], etc
with window 10 and overlap 5:
[0-9], [5-14], [10-19], [15-24], [20-29], etc.


Now that we understand the concept of buckets, the window and overlap parameters, the problem consist on returning the number of times that a bucket will contain any number of the numbers provided in the parameter "numbers".
So if we have a list like: [0, 10, 50] we need to calculate buckets at least from 0 to 50 depending on the window and overlap.
If window is 100, then we will have only 1 bucket (0-99) but if we have window 1 we will have 51 buckets (from 0 to 50).
For each bucket, count the number of times that a number in "numbers" is present in each bucket.
The return can be in tuples, in a dict, or whatever that can express which buckets have to be created and how many times a number falls in each bucket.

## Examples:
```
$ python histogram.py -n 0 1 2 3 4 5 6 7 8 20 50 -w 10 -o 0
{0: 9, 10: 0, 20: 1, 30: 0, 40: 0, 50: 1}
$ python histogram.py -n 0 1 2 3 4 5 6 7 8 12 -w 1 -o 0
{0: 1, 1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1, 7: 1, 8: 1, 9: 0, 10: 0, 11: 0, 12: 1}
$ python histogram.py -n 1 2 3 4 14 20 23 24 -w 15 -o 8
{0: 5, 7: 2, 14: 4, 21: 2}
```

## Tests:
```
$ make test
```
