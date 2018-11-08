import app from app
import urllib.request,json
from .models import article

Article = article.Article

api_key=app.config['API_KEY']
base_url = app.config["ARTICLE_API_BASE_URL"]


def get_article(category):
    '''
    Function that gets the json response to our url request
    '''
    get_article_url = base_url.format(category,api_key)

    with urllib.request.urlopen(get_article_url) as url:
        get_article_data = url.read()
        get_article_response = json.loads(get_article_data)

        article_results = None

        if get_article_response['results']:
            article_results_list = get_article_response['results']
            article_results = process_results(article_results_list)


    return article_results