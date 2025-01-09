from selenium import webdriver
from selenium.webdriver.chrome.options import Options

class UrlReader2:
    def __init__(self):
        self.user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36'
        opts = Options()
        opts.add_argument(f"user-agent={self.user_agent}")
        opts.add_argument("--disable-blink-features=AutomationControlled")
        self.driver = webdriver.Chrome(options=opts)

    def read_url(self, url):
        try:
            self.driver.get(url)
            page_source = self.driver.page_source
            return page_source
        except Exception as e:
            print(f"Error downloading page: {str(e)}")
            return None

    def close(self):
        self.driver.quit()
