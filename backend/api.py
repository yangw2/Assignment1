from data import NameQuery, NameInfo
import csv
import psycopg2
import psqlConfig as config

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
    
    def getNameData(connection, name, years) :
       
        try:
            cursor = connection.cursor()
            query = "SELECT * FROM childnames WHERE childName=%s INTERSECT SELECT * FROM childnames WHERE yearOfBirth=%s INTERSECT SELECT * FROM childnames WHERE sex=%s INTERSECT SELECT * FROM childnames WHERE ethnicity=%s INTERSECT SELECT * FROM childnames WHERE amountNames=%s ORDER BY childName ASC"
            cursor.execute(query, (name,years))
            return cursor.fetchall()

        except Exception as e:
            print ("Something went wrong when executing the query: ", e)
            return None