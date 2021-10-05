import scrapy


class AddgeneSpider(scrapy.Spider):
    # scraper name
    name = 'addgene'
    # allowed domain
    allowed_domains = ['www.addgene.org']
    start_urls = ['https://www.addgene.org/10675/sequences/']

    # Parse the response of start_urls 
    def parse(self, response):
        # response.text - response string
        # response.body - binary data before decoding
        # response.xpath(...) - get the result given xpath
        # response.extract() - extract 'data' of selector object
        geneFull = response.xpath('//*[@id="addgene-full"]/ul/li/div/div/div[2]/textarea/text()')
        genePartial = response.xpath('//*[@id="addgene-partial"]/ul/li/div/div/div[2]/textarea/text()')
        print(geneFull.extract())
