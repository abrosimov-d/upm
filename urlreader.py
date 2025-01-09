class UrlReader:
    def __init__(self):
        pass

    def read_url(self, url):
        try:
            import urllib.request
            response = urllib.request.urlopen(url)
            return response.read().decode('utf-8')
        except Exception as e:
            return f"Error reading URL: {str(e)}"