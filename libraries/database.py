import pyodbc 

class Database:
    def __init__(self, server, database):
        self.__server = server
        self.__database = database
    
    def connect(self):
        try:
            connection = pyodbc.connect('DRIVER={SQL Server};SERVER=' + self.__server + ';DATABASE=' + self.__database)
            connection.autocommit = True

            return connection
        except pyodbc.Error as ex:
            sqlstate = ex.args[0]
            if sqlstate == '28000':
                print("Failed to establish a connection to the database.")

    def executeTransaction(self, queries):
        connection = self.connect()
        connection.autocommit = False
        cursor = connection.cursor()

        for query in queries: 
            cursor.execute(query)

        connection.commit()

        return cursor.rowcount

    def execute(self, query, params=None):
        connection = self.connect()

        cursor = connection.cursor()
        cursor.execute(query)

        if autocommit:
            cursor.commit()

        return cursor.rowcount

    def getBatch(self, query, params=None, listIndex=0, batchSize=20):
        rows = []
        connection = self.connect()

        cursor = connection.cursor()
        if params is not None: 
            cursor.execute(query,params)
        else:
            cursor.execute(query)

        cursor.skip(listIndex)
        
        for row in cursor.fetchmany(batchSize):
            rows.append(row)
        
        return rows        

    def select(self, query, params=None): 
        rows = []
        connection = self.connect()

        cursor = connection.cursor()
        if params is not None: 
            cursor.execute(query,params)
        else:
            cursor.execute(query)

        for row in cursor.fetchall():
            rows.append(row)
        
        return rows
    