import unittest
from utils.configmanager import Config

class TestConfig(unittest.TestCase):
 
    def setUp(self):
        pass
 
    def testInitialisation(self):
        self.assertTrue(Config)

    def testAppSettings(self):
        pass
    
    def testConnections(self):
        self.assertTrue(Config.connections("DATABASE_SERVER"))
        self.assertTrue(Config.connections("DATABASE_NAME"))
 
if __name__ == '__main__':
    unittest.main()