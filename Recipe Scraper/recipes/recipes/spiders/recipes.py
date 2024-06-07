import scrapy


class RecipesSpider(scrapy.Spider):
    name = "recipes"
    allowed_domains = ["eatthegains.com"]
    start_urls = ["https://eatthegains.com/chicken-and-broccoli-stir-fry/#recipe"]

    # For individual books on an individual page
    def parse(self, response):
        ingredients = response.css("article.product_pod")
        for book in books:
            yield {
                "name": book.css("h3 a::text").get(),
                "price": book.css("div.product_price .price_color::text").get(),
                "url": book.css("h3 a").attrib["href"],
            }
