from data import NameQuery, NameInfo

#This function will format the name information list created above, and transform it into a NameQuery object, which we will use to 
#handle user requests in an efficient manner.
#input: a list of the desired name info
#output: a NameQuery object containing the target information
def createNameQuery(name, yearRangeStart, yearRangeEnd, gender, race, amountNames, sortingStyle) :
    #this object will be implemented later
    nq = NameQuery(name,yearRangeStart,yearRangeEnd,gender,race,amountNames,sortingStyle)
    return nq

#This function is the top-level function that will take in a nameQuery and output the final sorted list of names
#It does little on its own but calls the below functions that get the actual data
def createQueryResults(nameQuery):
    #object implemented later
    nameInfoList = [NameInfo()]
    return nameInfoList

#This function will take in a nameQuery object, and search through the database of names for names that fit
#the specified parameters. 
#It will output a list of all the names matching the parameters. If gender and race are not specified, then 
#names are lumped together if they are the same name regardless of gender or race
def searchNames(NameQuery) :
    allMatches = []
    return allMatches

#This function sorts the results from searchNames into proper order from the information from nameQuery
#Returns the sorted list containing nameInfo classes
def sortNameResults(NameQuery, nameInfoList) :
    return nameInfoList


#This function will set the list of name results returned to the desired length - if the user is just 
#curious about one name, then the list length will be one. The output is a trimmed list, the input is an untrimmed list 
#and the nameQuery object
def truncateNameResults(NameQuery, nameInfoList) :
    return nameInfoList

