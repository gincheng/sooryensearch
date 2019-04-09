import scrapy

class crawler(scrapy.Spider):
    name = "craigslist"
    custom_settings = {
        'CLOSESPIDER_ITEMCOUNT':1000,
        'CONCURRENT_REQUESTS' : 1,
        'CONCURRENT_ITEMS' :1
    }
    start_urls = [
        'https://newyork.craigslist.org/search/bka'
    ]

    def parse(self, response): 
        for item in response.css("body section.page-container form div.content ul.rows li.result-row"):
            yield {
                'name' : item.css("p.result-info a::text").get(),
                'price' : item.css("p.result-info span.result-price::text").get(),
                'link' : item.css("p.result-info a::attr(href)").get()
            }

        next_page = response.css("div.search-legend.bottom span.buttons a.button.next::attr(href)").get()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)
        