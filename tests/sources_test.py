import unittest
from models import Sources

Sources = sources.Sources


class sources_test(unittest.TestCase):
    '''
    this function creates an object of the Sources class before each and every tesy
    '''
    def setUp(self):
        self.new_source = Sources(
            'ABC-news', 'ABC-news','dk', 'https://abc.com', 'us')

    def test_instance(self):
        '''
        this is a function to assert whether the instance is really an instance of our class
        '''
        self.assertTrue(isinstance(self.new_source, Sources))

if __name__ == '__main__':
    unittest.main()