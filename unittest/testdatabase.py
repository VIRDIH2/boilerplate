import unittest
from libraries.database import Database
from utils.configmanager import Config

class TestDatabase(unittest.TestCase):
 
    def setUp(self):
        pass
 
    def testConnect(self):
        database = Database(Config.connections("DATABASE_SERVER"), Config.connections("DATABASE_NAME"))
        database.connect()
        self.assertEqual(True, True)
 
if __name__ == '__main__':
    unittest.main()