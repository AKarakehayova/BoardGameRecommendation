import scrapy
import io

class GamesCrawler(scrapy.Spider):
    name = "games"
    custom_settings = {
        'DEPTH_LIMIT': '200',
    }

    def start_requests(self):
        urls = [
            'https://boardgamegeek.com/browse/boardgame'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        names = response.xpath('//tr[@id="row_"]//td[3]//a/text()').extract()
        file_name = 'games.txt'
        with io.open(file_name, "a", encoding="utf-8") as f:
            f.writelines("\n".join(names))

        next_page = response.css('div.fr').xpath('//a[@title="next page"]/@href').extract_first()
        if next_page:
            url = response.urljoin(next_page)
            yield scrapy.Request(url, self.parse)