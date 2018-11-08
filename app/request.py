import app from app
import urllib.request,json
from .models import article

Sources = sources.Sources

api_key=app.config['API_KEY']
base_url = app.config["SOURCES_URL"]


def get_sources(category):
    '''
    a function that returns sources with category passed in as a parameter
    '''
    full_url = base_url.format(category,api_key)
    with urllib.request.urlopen(full_url) as url:
        source_data = url.read()
        json_source_data = json.loads(source_data)
        # print(json_source_data)

        source_list = None

        if json_source_data['sources']:
            json_lib = json_source_data['sources']
            source_list = process_sources(json_lib)

    return source_list

def process_results(sources_list):
    '''
    Function  that processes the sources result and transform them to a list of Objects

    Args:
        sources_list: A list of dictionaries that contain sources details

    Returns :
        sources_results: A list of sources objects
    '''
    sources_results = []
    for sources_item in sources_list:
        id = sources_item.get('id')
        name = sources_item.get('original_name')
        desc = sources_item.get('desc')
        poster = sources_item.get('poster_path')
        country =sources_item.get('country')
        url = sources_item.get('url')

        if poster:
            sources_object = sources(id,name,desc,poster,country,url)
            sources_results.append(sources_object)

    return sources_results    