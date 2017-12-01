import scrapy
class TestSpider(scrapy.Spider):
    name = "test"

    start_urls = [
        "https://fantasy.premierleague.com/drf/bootstrap-static",
    ]

    def parse(self, response):
        filename = response.url.split("/")[-1] + '.html'
        with open(filename, 'wb') as f:
            f.write(response.body)
            
            
class TestSpider(scrapy.Spider):
    name = "leagueTABLEtop10K"
    start_urls = ["https://fantasy.premierleague.com/a/leagues/standings/313/classic?phase=1&lsPage=" % 1]
    def __init__(self):
        self.page_number = 1

    def start_requests(self):
        # generate page IDs
        for i in range (self.page_number,5, -1):
            yield Request(url = URL % i, callback=self.parse)

    def parse(self, response):
        filename = response.url.split("/")[-1] + '.html'
        with open(filename, 'wb') as f:
            f.write(response.body)
