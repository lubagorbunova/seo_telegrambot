from Page_info import Page_processor

page1 = Page_processor('https://segor.ru/')
page1.load_text()
page1.extract_keywords()

keywords = page1.keywords
print(keywords)