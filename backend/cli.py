from api import *
from data import NameQuery, NameInfo

def main():
    testingAPI = BabyNameAPI("Popular_Baby_Names.csv")
    print("API TESTER \nEnter 'Exit' to exit. Enter 'Help' for help.")
    userInput = ""
    while userInput.lower() != "exit":
        userInput = input("Prompt:")
        if (userInput.lower() == "create results"):
            print(testingAPI.createQueryResults(NameQuery()))
        elif (userInput.lower() == "create query"):
            print(testingAPI.createNameQuery("Jeff", 2011, 2012, 'M', "White", 1, 1))
        elif (userInput.lower() == "help"):
            print("Enter 'create results' or 'create query' to test functionality. Enter 'exit' to exit.")
        elif (userInput.lower() != "exit"):
            print("Invalid command, enter 'help' for a list of commands or 'exit' to exit")
        

main()