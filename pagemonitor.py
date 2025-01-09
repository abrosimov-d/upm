from urlreader2 import UrlReader2
from extractor import HTMLTextExtractor
from snapshot import Snapshot

class PageMonitor:
    def __init__(self, config):
        self.config = config

    def update_pages(self):
        page_id = 0
        for url in self.config.pages:
            print(url)
            reader = UrlReader2()
            result = reader.read_url(url)
            html_extractor = HTMLTextExtractor()
            result = html_extractor.extract_text(result)
            snapshot = Snapshot(url, page_id, 'empty_title', 'empty_time', result)
            page_id = page_id + 1
            snapshot.store_to_db()

    def check_page(self, url):
        try:
            # Placeholder for actual page checking logic
            pass
        except Exception as e:
            print(f"Error checking page: {e}")

    def get_changes(self):
        # Placeholder for detecting changes
        pass

    def notify(self):
        # Placeholder for notification logic
        pass
