import unittest
from models import article
Article = article.article

class ArticleTest(unittest.TestCase):
    '''
    Test class to  test the behaviour of article class
    '''
     def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_article = Article(1234,'bbc news','A thrilling new world','new world','John','url','urlToImage','publishedAt')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_article,Article))

if __name__ == '__main__':
    unittest.main()