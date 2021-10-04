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
        # response.xpath(...) - get the regx result
        # response.extract() - extract property value of selector object data
        gene = response.xpath('//*[@id="addgene-full"]/ul/li/div/div/div[2]/textarea/text()') #//*[@id="addgene-partial"]/ul/li/div/div/div[2]/textarea
        print(gene.extract())
