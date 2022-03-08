import scrapy


class FarfetchWomenSpider(scrapy.Spider):
    name = 'farfetch_women'
    allowed_domains = ['www.farfetch.com']
    start_urls = ['https://www.farfetch.com/fr/shopping/women/bags-purses-1/items.aspx']

    def parse(self, response):
        womenBags = response.xpath('//*[@id="slice-container"]/div[3]/div[2]/div[2]/div/div[1]/ul/div')
        for bag in womenBags:
            try:
                # self.get_products(bag)
                yield  {
                    "product-page-url": bag.xpath('@itemid').extract(),
                    "image": bag.xpath('a/div/link/@href').extract(),
                    "brand": bag.xpath('a/div')[1].xpath('div/p/text()')[0].extract(),
                    "name":  bag.xpath('a/div')[1].xpath('div/p/text()')[1].extract(),
                    "price":  bag.xpath('a/div')[1].xpath('div/p/text()')[2].extract()
                }
            except Exception as e:
                print("error",e)
