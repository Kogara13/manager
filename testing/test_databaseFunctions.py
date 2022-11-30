import unittest
from databaseFunctions import addPassword
from databaseFunctions import deleteSelectedPassword

class TestDatabaseInput(unittest.TestCase):
    def test_add(self):
           
        # Test to see that data is successfully added to the database. Returns the number of rows with provided Account name in a tuple. 
        self.assertEqual(addPassword('test0', 'pass0', 'pass0'), ('test0', 'pass0'))
        self.assertEqual(addPassword('test1', 'pass1', 'pass1'), ('test1', 'pass1'))
        self.assertEqual(addPassword('test2', 'pass2', 'pass2'), ('test2', 'pass2'))
        self.assertEqual(addPassword('test3', 'pass3', 'pass3'), ('test3', 'pass3'))
        self.assertEqual(addPassword('test4', 'pass4', 'pass4'), ('test4', 'pass4'))
        self.assertEqual(addPassword('test5', 'pass5', 'pass5'), ('test5', 'pass5'))
        self.assertEqual(addPassword('test6', 'pass6', 'pass6'), ('test6', 'pass6'))
        self.assertEqual(addPassword('test7', 'pass7', 'pass7'), ('test7', 'pass7'))
        self.assertEqual(addPassword('test8', 'pass8', 'pass8'), ('test8', 'pass8'))
        self.assertEqual(addPassword('test9', 'pass9', 'pass9'), ('test9', 'pass9')) 
           
        #Test to see that data is successfully removed from the database. Returns the number of rows with provided Account name in a tuple.
        self.assertEqual(deleteSelectedPassword('test0', 'Y'), (0,))
        self.assertEqual(deleteSelectedPassword('test1', 'Y'), (0,))
        self.assertEqual(deleteSelectedPassword('test2', 'Y'), (0,))
        self.assertEqual(deleteSelectedPassword('test3', 'Y'), (0,))
        self.assertEqual(deleteSelectedPassword('test4', 'Y'), (0,))

        #Test to see that deletion from database can be suspended. Returns the number of rows with provided Account name in a tuple.
        self.assertEqual(deleteSelectedPassword('test5', 'N'), (1,))
        self.assertEqual(deleteSelectedPassword('test6', 'n'), (1,))
        self.assertEqual(deleteSelectedPassword('test7', 'N'), (1,))
        self.assertEqual(deleteSelectedPassword('test8', 'n'), (1,))
        self.assertEqual(deleteSelectedPassword('test9', 'N'), (1,))
        
         
         
