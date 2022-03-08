import scrapy

from ..items import FarfetchItem

class FarfetchSpider(scrapy.Spider):
    name = 'farfetch'
    allowed_domains = ['www.farfetch.com']
    start_urls = ['https://www.farfetch.com/fr/shopping/men/shoes-2/items.aspx']


    def get_products(self, shoes):
        """
        The callback method gets the response from each article url.
        It fetches the article comment obj, creates a list of comments, and returns dict with the list of comments and article id.
        """
        FarfetchItem(
            product_page_url =  shoes.xpath('@itemid').extract(),
            image = shoes.xpath('a/div/link/@href').extract(),
            brand = shoes.xpath('a/div')[1].xpath('div/p/text()')[0].extract(),
            name = shoes.xpath('a/div')[1].xpath('div/p/text()')[1].extract(),
            price =   shoes.xpath('a/div')[1].xpath('div/p/text()')[2].extract()
        ) 
            

    def parse(self, response):
        menShoes = response.xpath('//*[@id="slice-container"]/div[3]/div[2]/div[2]/div/div[1]/ul/div')
        for shoes in menShoes:
            try:
                # self.get_products(shoes)
                yield  {
                    "product-page-url": shoes.xpath('@itemid').extract(),
                    "image": shoes.xpath('a/div/link/@href').extract(),
                    "brand": shoes.xpath('a/div')[1].xpath('div/p/text()')[0].extract(),
                    "name":  shoes.xpath('a/div')[1].xpath('div/p/text()')[1].extract(),
                    "price":  shoes.xpath('a/div')[1].xpath('div/p/text()')[2].extract()
                }
            except Exception as e:
                print("error",e)
        # print("page completed")
            
        
