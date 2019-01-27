import scrapy
import re

class CommentsSpider(scrapy.Spider):
    name = "comments"

    def start_requests(self):
        urls = [
            'https://boardgamegeek.com/thread/2132253/picking-my-first-dudes-map-game?fbclid=IwAR1sHUDQGYCq-0jCyVgcPXau1NNbwb88b9zFsvvIalxFPDINbaOWiQ6MuVI',
            'https://boardgamegeek.com/thread/2124917/easy-fun-short-downtime-4-5-players?fbclid=IwAR3XspRkNlw10-fdIv7e_Q3kW8JhJgjZKR979-7-9NMF1kjmHcx4AokU7-Q',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = 'comments-%s.html' % page
        result = ''
        for comment in response.css('div.article'):
            text = comment.css('dd.right').extract_first()
            cleaner = re.compile('<[^>]+>')
            cleanest = re.compile(r'[\n\r\t]')
            text = re.sub(cleaner, ' ', text)
            text = re.sub(cleanest, '', text)
            yield {
                comment.css('div.username a::text').extract_first() : text
            }