import scrapy
import csv


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
        parsed_data = []
        for divan in divans:
            # yield {
            #     'name': divan.css('div.wYUX2 span::text').get(),
            #     'price': divan.css('div.q5Uds span::text').get(),
            #     'url': divan.css('a').attrib['href']
            # }
            name_t = divan.css('div.wYUX2 span::text').get()
            price_t = divan.css('div.q5Uds span::text').get()
            url_t = divan.css('a').attrib['href']
            parsed_data.append([name_t, price_t, url_t])

        with open("divan_svet.csv", 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['Название товара', 'Цена товара', 'Ссылка на товар'])
            writer.writerows(parsed_data)