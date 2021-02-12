import unittest
import csv

from histogram import buckets_histogram


class TestHistogram(unittest.TestCase):

    def test_combinations(self):
        with open('combinations.csv') as fd:
            csv_reader = csv.DictReader(fd, delimiter=';')
            for row in csv_reader:
                nums = list(map(int, row['nums'].split(' ')))
                w = int(row['w'])
                o = int(row['o'])
                expected_histogram = eval(row['histogram'])
                histogram = buckets_histogram(nums, w, o)
                self.assertEqual(histogram, expected_histogram)
