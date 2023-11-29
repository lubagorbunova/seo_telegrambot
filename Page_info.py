import requests
from bs4 import BeautifulSoup
import spacy

class Page_processor():
    """
    stores information about a single web page
    """
    def __init__(self, url) -> None:
        self.url = url
        self.page_name = ''
        self.raw_text = ''
        self.processed_text = ''
        self.keywords = []
        self.unique_keywords = None
        self.inside_links = []
        self.search_position = None

    
    def load_text(self):
        """
        loads text from the page
        """
        response = requests.get(url=self.url, headers={'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'})
        main_bs = BeautifulSoup(response.text, 'lxml')
        
        self.raw_text = main_bs.text


    def extract_keywords(self):
        """
        extracts n keywords from the given text
        """
        nlp = spacy.load("ru_core_news_sm")
        doc = nlp(self.raw_text)
        keywords = doc.ents
        for word in keywords:
            self.keywords.append(str(word))
        self.unique_keywords = set(self.keywords)

    def process_text(self):
        """
        removes extra data
        """
        pass

    def find_inside_links(self):
        """
        finds all links inside the page
        """
        pass