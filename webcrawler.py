import requests
import re

class WebCrawler:

    def __init__(self):
        self.url_visited = []

    def crawler(self, start_url):
        queue = [start_url]
        self.url_visited.append(start_url)

        while queue:

            actual_url = queue.pop(0)
            print(actual_url)

            actual_url_html = self.get_url(actual_url)
            print(actual_url_html)

            for web in self.get_urls_from_text(actual_url_html):
                if web not in self.url_visited():
                    self.url_visited.append(web)
                    queue.append(web)

    def get_urls_from_text(self, text):
        return re.findall("https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+", text)

    def get_url(self, url):
        url_text = ''

        try:
            url_text = requests.get(url).text

        except Exception as e:
            pass

        return url_text

if __name__ == '__main__':

    crawler = WebCrawler()
    crawler.crawler('https://cnnespanol.cnn.com/')


