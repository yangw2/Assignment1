
#This function is the top-level function that will sequentially call each other function in the API. It sets up
#the list of requested data from the inputs. Some of the inputs can be blank, but they are, in order,
#the name of interest, the year range of interest, the gender, the race, the amount of names desired to be generated, and 
#the style of sorting desired by the user. The output is all of these inputs formatted into a class called "nameInfo", which can
#easily be passed to other functions 
#this function will mostly just call 4 other functions
def handleUserSearch(name, yearRange, gender, race, amountNames, sortingStyle) :
    #object implemented later
    nameInfoNew = new nameInfo(name, yearRange, gender, race, amountNames, sortingStyle)
    return nameInfo

#This function will format the name information list created above, and transform it into a NameQuery object, which we will use to 
#handle user requests in an efficient manner.
#input: a list of the desired name info
#output: a NameQuery object containing the target information
def createNameQuery(nameInfo) :
    #this object will be implemented later
    nq = new NameQuery(nameInfo)
    return nq

#This function will take in a nameQuery object, and search through the database of names for names that fit
#the specified parameters. 
#It will output a list of all the names matching the parameters. If gender and race are not specified, then 
#names are lumped together if they are the same name regardless of gender or race
def searchNames(NameQuery) :
    allMatches = []
    return allMatches

#This function sorts the results from searchNames into proper order from the information from nameQuery
#Returns the sorted list containing nameInfo classes
def sortNameResults(NameQuery, List<nameInfo>) :
    return List<nameInfo>


#This function will set the list of name results returned to the desired length - if the user is just 
#curious about one name, then the list length will be one. The output is a trimmed list, the input is an untrimmed list 
#and the nameQuery object
def truncateNameResults(NameQuery, List<nameInfo>) :
    return List<nameInfo>



