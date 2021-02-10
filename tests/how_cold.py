import unittest

class TempTracker(object):
    """
    Temperature Tracker, Implement methods to track the max, min and mean.

    TempTracker clas with following methods
    insert() - records a new temperature
    get_max() - returns highest 
    get_min() - returns lowest
    get_mean() - returns mean
    get_mean() should return a float, but the rest of the getter functions can return integers. 
    
    Temperatures will all be inserted as integers. 
    We'll record our temperatures in Fahrenheit, so we can assume they'll all be in the range 0..110

    """

    def __init__(self):
        
        self.count = 0
        self.min = 111
        self.max = -1
        self.sum = 0

    def insert(self, value):
        """
        Records a new temperature

        :param int value: the temperature in Fahrenheit
        """

        if not isinstance(value, int):
            raise ValueError

        if value < 0 or value > 110:
            raise IndexError

        self.count += 1

        self.min = min(self.min, value)
        self.max = max(self.max, value)

        self.sum += value

    def get_max(self):
        """
        Returns the highest temperature we have seen so far

        :return: temperature
        :rtype: int
        """

        max = self.max
        if max == -1:
            max = None
        return max

    def get_min(self):
        """
        Returns the lowest temperature we have seen so far

        :return: temperature
        :rtype: int
        """

        min = self.min
        if min == 111:
            min = None
        return min

    def get_mean(self):
        """
        Returns the mean of all temperatures we have seen so far

        :return: temperature
        :rtype: float
        """

        try:
            return self.sum / float(self.count)
        except ZeroDivisionError:
            print("ZeroDivisionError: float division by zero")



class TestTempTracker(unittest.TestCase):
    
    def _test_tracker(self, temps, min, max, mean):
        tracker = TempTracker()
        for temp in temps:
            tracker.insert(temp)
        print("")
        print("Test: temps = %s" % temps)
        print(" min %s max %s" % (tracker.get_min(), tracker.get_max()))
        self.assertTrue(tracker.get_min() == min)
        self.assertTrue(tracker.get_max() == max)
        print(" mean %s" % (tracker.get_mean()))
        self.assertTrue(tracker.get_mean() == mean)

    def test_none(self):
        self._test_tracker([], None, None, None)

    def test_zeros(self):
        self._test_tracker([0], 0, 0, 0)

    def test_one(self):
        self._test_tracker([0, 1], 0, 1, 0.5)

    def test_two(self):
        self._test_tracker([0, 1, 1], 0, 1, 2 / 3.0)

    def test_three(self):
        self._test_tracker([0, 1, 1, 2], 0, 2, 4 / 4.0)

    def test_minmax(self):
        tracker = TempTracker()
        self.assertRaises(Exception, tracker.insert, -1)
        self.assertRaises(Exception, tracker.insert, 111)
