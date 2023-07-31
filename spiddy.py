from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

class BlogSpider(CrawlSpider):
    name = 'nytimes'
    allowed_domains = ['nextinvestors.com', 'catalysthunter.com', 'wise-owl.com','finfeed.com']
    start_urls = ['https://www.nextinvestors.com/']

    custom_settings = {
        'USER_AGENT': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36',
        'FEEDS': { 'data.csv': { 'format': 'csv', 'overwrite': True}}
        
    }

    rules = (
        Rule(LinkExtractor(allow=r''), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        # Extract the page title
        page_title = response.css('title::text').get()

        # Calculate link depth
        link_depth = response.meta.get('depth', 0)

        # Yield the scraped data
        yield {
            'url': response.url,
            'title': page_title,
            'link_depth': link_depth
        }