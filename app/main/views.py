from flask import render_template
from . import main

@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    # Getting popular movie
    popular_sources = get_sources('popular')
    print(popular_sources)
    title = 'Home - source'
    return render_template('index.html', title=name,popular = popular_sources)

@main.route('/source/<source_id>')
def source(source_id):

    '''
    View movie page function that returns the movie details page and its data
    '''
    return render_template('source.html',id = news_id)