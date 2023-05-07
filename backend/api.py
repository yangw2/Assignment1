from data import NameQuery, NameInfo
import csv


class BabyNameAPI:
    #Sets up the default values, so if the user doesn't specify what a particular parameter is, 
    #we can use these default values to still run the SQL Queries
    
    def __init__(self):
        self.years = [2014,2015,2016,2017,2018,2019]
        self.sexes = ["MALE","FEMALE"]
        self.ethnicities = ["ASIAN AND PACIFIC ISLANDER",
                             "HISPANIC", "BLACK NON HISPANIC", "WHITE NON HISPANIC"]
        self.names = []
        self.amountToGenerate = [20]
        self.sortOrder = ["DESC"]


    def set_years(self, years):
        self.years = years

    def set_sexes(self, sexes):
        self._sexes = sexes

    def set_ethnicities(self, ethnicities):
        self.ethnicities = ethnicities

    def set_names(self, names):
        self.names = names

    def set_amountToGenerate(self, amountToGenerate):
        self.amountToGenerate = amountToGenerate

    def set_sortOrder(self, sortOrder):
        self.sortOrder = sortOrder


    
    def connect():
    '''
    Establishes a connection to the database with the following credentials:
        user - username, which is also the name of the database
        password - the password for this database on perlman

    Returns: a database connection.

    Note: exits if a connection cannot be established.
    '''
    try:
        connection = psycopg2.connect(database=config.database, user=config.user, password=config.password, host="localhost")
        #debugging
        print("beep boop! connected!")
    except Exception as e:
        print("Connection error: ", e)
        exit()
    return connection
    
        
#     def __init__(self,filename):
#         with open(filename, newline='') as namesFile:
#             self.namesList = list(csv.DictReader(namesFile))
#     #at this point in the code: we have a list of dictionaries, keyed to each name/year/ethnicity/sex/number combo

#     def getNamesRankedAbove(self, lowerVal) 
#         '''
#         This function takes as an input a lower value for names, and returns all name instances (name with year, sex, ethnicity, and value)
#         with values equal to or greater than the lower value.
#         Input: a lower value
#         Output: a list of names that have greater or equal value than the input value
#         '''
#         names = []
#         #make sure the input is valid
#         if lowerVal <= 10 :
#             return names
#         for name in self.namesList :
#             amount = float(name["Count"])
#             if amount >= lowerVal :
#                 names.append(name)
#         return names
    
#     def getNamesFromYears(self, yearList) :
#         '''
#         Input: A list of years (ints) that the desired name objects should come from
#         Output: a list of names that come from the selected year(s) 
#         '''
#         names = []
#         #no need to sanitize input
#         for name in self.namesList :
#             year = int(name["Year of Birth"])
#             if year in yearList :
#                 names.append(name)
#         return names
    
#     def getEthnicities(self, ethnicitiesList) :
#         '''
#         Input: A list of ethnicities (strings) that the desired name objects should come from
#         Output: a list of names that are labeled as the selected ethinicities(s) 
#         '''
#         names = []
#         #no need to sanitize input
#         for name in self.namesList :
#             eth = str(name["Ethnicity"])
#             if eth in ethnicitiesList :
#                 names.append(name)
#         return names

#     def getNamesFromName(self, nameInput):
#         '''
#         Input: A string for the desired name
#         Output: All entries in the dataset for that name
#         '''
#         names = []
#         for name in self.namesList:
#             if (str(name["Child's First Name"]).lower() == nameInput.lower()):
#                 names.append(name)
#         return names
    
#     def getNamesBySex(self, sexInput):
#         '''
#         Input: The desired sex for the child's name
#         Output: All entries of that sex
#         '''
#         names = []
#         for name in self.namesList:
#             if (str(name["Gender"]).lower() == sexInput.lower()):
#                 names.append(name)
#         return names


# '''
# Commented out everything below this, it's from our older API but I don't want to just delete the code in case we need an 
# easy way to access it earlier. I know we could also use GIT, but it's not stuff I necessarily wrote so I'm not super comfy
# just deleting it now.
# '''
        
# #     #This function will format the name information list created above, and transform it into a NameQuery object, which we will use to 
# #     #handle user requests in an efficient manner.
# #     #input: a list of the desired name info
# #     #output: a NameQuery object containing the target information
# #     def createNameQuery(self,name, yearRangeStart, yearRangeEnd, gender, race, amountNames, sortingStyle) :
# #         #this object will be implemented later
# #         nq = NameQuery(name,yearRangeStart,yearRangeEnd,gender,amountNames,race,sortingStyle)
# #         return nq

# #     #This function is the top-level function that will take in a nameQuery and output the final sorted list of names
# #     #It does little on its own but calls the below functions that get the actual data
# #     def createQueryResults(self,nameQuery):
# #         #object implemented later
# #         nameInfoList = [NameInfo()]
# #         return nameInfoList

# #     #This function will take in a nameQuery object, and search through the database of names for names that fit
# #     #the specified parameters. 
# #     #It will output a list of all the names matching the parameters. If gender and race are not specified, then 
# #     #names are lumped together if they are the same name regardless of gender or race
# #     def searchNames(self,NameQuery) :
# #         allMatches = []
# #         return allMatches

# #     #This function sorts the results from searchNames into proper order from the information from nameQuery
# #     #Returns the sorted list containing nameInfo classes
# #     def sortNameResults(self,NameQuery, nameInfoList) :
# #         return nameInfoList


# #     #This function will set the list of name results returned to the desired length - if the user is just 
# #     #curious about one name, then the list length will be one. The output is a trimmed list, the input is an untrimmed list 
# #     #and the nameQuery object
# #     def truncateNameResults(self,NameQuery, nameInfoList) :
# #         return nameInfoList

# # # def main():
# # #     testingAPI = BabyNameAPI("Popular_Baby_Names.csv")
# # #     testList = []
# # #     for nameInfo in testingAPI.namesListUnprocessed:
# # #         if nameInfo["Child's First Name"] == "Aidan":
# # #             print(nameInfo)

# # # main()