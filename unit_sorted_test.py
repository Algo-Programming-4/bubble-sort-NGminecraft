import sorting
import random
import unittest


class Test(unittest.TestCase):
    def test_sorted(self):
        for _ in range(10):
            nums = [random.randint(1,100) for x in range(random.randint(1,100))]
            result =  sorting.bubble(nums)
            self.assertEqual(result, sorted(nums))
      
if __name__ == "__main__":
    Test().test_sorted()
