import unittest
from app.models import article
Article = article.Article

class ArticleTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Article class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_article = Article(1234,'bbc news','A thrilling new world','new world','John','url','urlToImage','publishedAt')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_article,Article))

