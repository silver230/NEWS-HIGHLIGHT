from flask import render_template
from . import main
from ..requests import get_sources,get_articles
from ..models import Source,Article

# Views
@main.route('/')
def index():
    '''
    View root page function that returns the page and and its data
    '''

    # Getting breaking news source
    general_source = get_sources('general')
    sports_source = get_sources('sports')
    technology_source = get_sources('technology')
    entertainment_source = get_sources('entertainment')
    business_source = get_sources('business')
    science_source = get_sources('science')
    title = 'Home - Welcome to the NewsHighlights '
    return render_template('index.html',title = title, general = general_source, sports = sports_source,technology =technology_source, entertainment = entertainment_source, business =business_source, science =science_source)

@main.route('/source/<id>')
def articles(id):
    '''
    view source page function that returns the source details page and its data
    '''
    
    articles = get_articles(id)

    return render_template('source.html',articles=articles)    
