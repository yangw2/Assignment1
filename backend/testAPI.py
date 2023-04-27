from api import *

import unittest

class APITester(unittest.TestCase) :

    # test cases for the names above method
    def test_Names_Above(self):
        lowerVal = 426
        api = BabyNameAPI("Popular_Baby_Names.csv")
        self.assertEqual(len(api.getNamesRankedAbove(lowerVal)),1) 
    
    def test_Names_Above_Negative(self):
        lowerVal = -1
        api = BabyNameAPI("Popular_Baby_Names.csv")
        self.assertEqual(len(api.getNamesRankedAbove(lowerVal)),0)

    def test_Names_Above_Too_Little(self):
        lowerVal = 8
        api = BabyNameAPI("Popular_Baby_Names.csv")
        self.assertEqual(len(api.getNamesRankedAbove(lowerVal)),0)

    # test cases for years method
    def test_Years_Method(self) :
        yearList = [2014,2015,2016,2017]
        api = BabyNameAPI("Popular_Baby_Names.csv")
        self.assertGreaterEqual(len(api.getNamesFromYears(yearList)), 1)

    def test_Years_Method_Below(self) :
        yearList = [2000]
        api = BabyNameAPI("Popular_Baby_Names.csv")
        self.assertEqual(len(api.getNamesFromYears(yearList)), 0)
        
    def test_Years_Method_Above(self) :
        yearList = [2024]
        api = BabyNameAPI("Popular_Baby_Names.csv")
        self.assertEqual(len(api.getNamesFromYears(yearList)), 0)



        


if __name__ == "__main__":
    unittest.main()      