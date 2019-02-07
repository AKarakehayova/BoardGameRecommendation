import scrapy
import io
import re

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
        geek_rating = response.xpath('//tr[@id="row_"]//td[4]/text()').extract()
        avg_rating = response.xpath('//tr[@id="row_"]//td[5]/text()').extract()
        num_votes = response.xpath('//tr[@id="row_"]//td[6]/text()').extract()

        size = len(names)
        crop_left = re.compile(r'[\n\t\t\t]')
        crop_right = re.compile(r'[\t\t]')
        for i in range(size):
            name = names[i]
            g_rating = geek_rating[i]
            a_rating = avg_rating[i]
            votes = num_votes[i]

            name = re.sub(crop_left, '', name)
            name = re.sub(crop_right, '', name)
            g_rating = re.sub(crop_left, '', g_rating)
            g_rating = re.sub(crop_right, '', g_rating)
            a_rating = re.sub(crop_left, '', a_rating)
            a_rating = re.sub(crop_right, '', a_rating)
            votes = re.sub(crop_left, '', votes)
            votes = re.sub(crop_right, '', votes)

            yield {
                "name" : name,
                "geek_rating" : g_rating,
                "avg_rating" : a_rating,
                "num_votes" : votes
            }

        next_page = response.css('div.fr').xpath('//a[@title="next page"]/@href').extract_first()
        if next_page:
            url = response.urljoin(next_page)
            yield scrapy.Request(url, self.parse)