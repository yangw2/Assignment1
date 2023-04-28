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


    #test cases for ethnicities method
    def test_Ethnicities(self) :
        ethnicitiesList = ["WHITE NON HISPANIC", "HISPANIC"]
        api = BabyNameAPI("Popular_Baby_Names.csv")
        self.assertGreaterEqual(len(api.getEthnicities(ethnicitiesList)), 1)
    
    def test_Ethnicities_Bad_String(self) :
        ethnicitiesList = ["BING BONG"]
        api = BabyNameAPI("Popular_Baby_Names.csv")
        self.assertEqual(len(api.getEthnicities(ethnicitiesList)), 0)
    
    def test_Ethnicities_Bad_Input(self) :
        ethnicitiesList = [1]
        api = BabyNameAPI("Popular_Baby_Names.csv")
        self.assertEqual(len(api.getEthnicities(ethnicitiesList)), 0)

    #test cases for first name searching method
    def test_Common_Name_Input(self):
        api = BabyNameAPI("Popular_Baby_Names.csv")
        self.assertGreaterEqual(len(api.getNamesFromName("Aidan")), 1)

    def test_Bad_String(self):
        api = BabyNameAPI("Popular_Baby_Names.csv")
        self.assertEqual(len(api.getNamesFromName("BALALBALSDFLABSDFL")), 0)

    #test cases for sex searching method
    def test_Male_Sex_Input(self):
        api = BabyNameAPI("Popular_Baby_Names.csv")
        self.assertGreaterEqual(len(api.getNamesBySex("Male")), 1)

    def test_Female_Sex_Input(self):
        api = BabyNameAPI("Popular_Baby_Names.csv")
        self.assertGreaterEqual(len(api.getNamesBySex("Female")), 1)

    def test_Bad_Sex_Input(self):
        api = BabyNameAPI("Popular_Baby_Names.csv")
        self.assertEqual(len(api.getNamesBySex("blahblah")), 0)

        


if __name__ == "__main__":
    unittest.main()      