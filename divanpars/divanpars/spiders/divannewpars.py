import scrapy


class DivannewparsSpider(scrapy.Spider):
    name = "divannewpars"
    allowed_domains = ["https://divan.ru"]
    start_urls = ["https://www.divan.ru/category/svet"]

    def parse(self, response):
        pages = response.css('a.PaginationLink')
        print('pages *********************************')
        url_pages = []
        for page in pages:
            url_pages.append(page.css('a').attrib['href'])
        url_pages = list(set(url_pages))
        for url_page in url_pages:
            print(url_page)
        # А вот как перебрать и прочитать страницы светильников пока не разобрался...

        divans = response.css('div._Ud0k')
        print('https://www.divan.ru/category/svet ********************************')
        print(str(len(divans)))
        for divan in divans:
            yield {
                'name': divan.css('div.wYUX2 span::text').get(),
                'price': divan.css('div.q5Uds span::text').get(),
                'url': divan.css('a').attrib['href']
            }

