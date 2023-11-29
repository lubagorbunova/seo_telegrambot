from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import requests
from bs4 import BeautifulSoup
from Page_info import Page_processor
   

class Search_Loader():
    """
    loads information about search input
    """
    def __init__(self) -> None:
        self.urls_list = []

    def load_search_list(self):
        """
        loads list of urls for this search
        """
        pass

    def get_page_position(self):
        """
        gets a position of the given url in the urls' list
        """
        pass

