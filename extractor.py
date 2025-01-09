from bs4 import BeautifulSoup

class HTMLTextExtractor:
    def __init__(self):
        self.text = ""

    def extract_text(self, html):
        soup = BeautifulSoup(html, 'html.parser')
        self.text = soup.get_text(separator=' ', strip=True)
        return self.text

    def get_text(self):
        return self.text
