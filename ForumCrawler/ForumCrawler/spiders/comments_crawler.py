import scrapy
import re

class CommentsSpider(scrapy.Spider):
    name = "comments"

    def start_requests(self):
        urls = [
            'https://boardgamegeek.com/thread/2132253/picking-my-first-dudes-map-game?fbclid=IwAR1sHUDQGYCq-0jCyVgcPXau1NNbwb88b9zFsvvIalxFPDINbaOWiQ6MuVI',
            'https://boardgamegeek.com/thread/2124917/easy-fun-short-downtime-4-5-players?fbclid=IwAR3XspRkNlw10-fdIv7e_Q3kW8JhJgjZKR979-7-9NMF1kjmHcx4AokU7-Q',
            'https://boardgamegeek.com/thread/2008425/best-two-player-game?fbclid=IwAR1q_PAAgiGhbtt93hqWT0a38Uf0G3O2QxPUyw1YPvgVXm9jVIit5JXhZ1w',
            'https://boardgamegeek.com/thread/1436356/highly-interactive-contentious-aggressive-thematic?fbclid=IwAR3BaYlDqG3tb0kUi3tXvHfU21Z-QFLeIWbSYXetLAK6PYkK030uI2Ri0mc'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        for comment in response.css('div.article'):
            text = comment.css('dd.right').extract_first()
            cleaner = re.compile('<[^>]+>')
            cleanest = re.compile(r'[\n\r\t]')
            text = re.sub(cleaner, ' ', text)
            text = re.sub(cleanest, '', text)
            yield {
                "user" : comment.css('div.username a::text').extract_first(),
                "comment" : text
            }

        pager = response.css('div.pager')
        if pager:
            next_page = pager.xpath('//a[@title="next page"]/@href').extract_first()
            if next_page:
                yield response.follow(next_page, self.parse)