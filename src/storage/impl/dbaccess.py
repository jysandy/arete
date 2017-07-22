import psycopg2

class database:
    def __init__(self, i_dbname, i_user, i_host, i_password):
        self.__dbname = i_dbname
        self.__user = i_user
        self.__host = i_host
        self.__password = i_password
        self.__connectstring = ''
        self.__parseconnectstring()
    
    def setdbname(self, entry):
        self.__dbname = entry
        self.__parseconnectstring()

    def setuser(self, entry):
        self.__user = entry
        self.__parseconnectstring()

    def sethost(self, entry):
        self.__host = entry
        self.__parseconnectstring()

    def setpassword(self, entry):
        self.__password = entry
        self.__parseconnectstring()

    def __parseconnectstring(self):
        self.__connectstring += "dbname='"
        self.__connectstring += self.__dbname
        self.__connectstring += "' user='"
        self.__connectstring += self.__user
        self.__connectstring += "' host='"
        self.__connectstring += self.__host
        self.__connectstring += "' password='"
        self.__connectstring += self.__password
        self.__connectstring += "'"

    def printconnectstring(self):
        print(self.__connectstring)

    def connecttodb(self):
        try:
            conn = psycopg2.connect(self.__connectstring)
            print("Connection Successful")
        except:
            print("I am unable to connect to that database")
