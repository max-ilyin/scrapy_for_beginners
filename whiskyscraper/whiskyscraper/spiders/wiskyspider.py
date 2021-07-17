import scrapy


class WiskySpider(scrapy.Spider):
    name = "wisky_spider"
    start_urls = ['https://www.whiskyshop.com/scotch-whisky?item_availability=In+Stock']

    def parse(self, response):
        for products in response.xpath('//div[@class="product-item-info"]'):
            try:
                yield {
                    'name': products.css('a.product-item-link::text').get(),
                    'price': products.css('span.price::text').get().replace('£', ''),
                    'link': products.css('a.product-item-link').attrib['href'],
                }
            except:
                yield {
                    'name': products.css('a.product-item-link::text').get(),
                    'price': 'sold out',
                    'link': products.css('a.product-item-link').attrib['href'],
                }