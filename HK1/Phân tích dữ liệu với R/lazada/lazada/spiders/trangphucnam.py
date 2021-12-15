import scrapy
from ..items import LazadaItem
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

class TrangphucnamSpider(scrapy.Spider):
    name = 'trangphucnam'
    def start_requests(self):
        chrome_options = Options()
        chrome_options.add_argument("--incognito")
        chrome_options.add_argument("--window-size=1920x1080")
        driver = webdriver.Chrome(chrome_options=chrome_options, executable_path="D:\chromedriver.exe")
        driver.get('https://www.lazada.vn/trang-phuc-nam/')
        link_elements = driver.find_elements_by_xpath('//*[@data-qa-locator="product-item"]//a[text()]')
        for link in link_elements:
            yield scrapy.Request(link.get_attribute('href'), callback=self.parse)
        time.sleep(3)
        driver.quit()

    def parse(self, response):
        name = response.xpath('//h1[@class="pdp-mod-product-badge-title"]/text()').get()
        sale_price = response.xpath('//span[@class="pdp-price pdp-price_type_normal pdp-price_color_orange pdp-price_size_xl"]/text()').get()
        initial_price = response.xpath('//span[@class="pdp-price pdp-price_type_deleted pdp-price_color_lightgray pdp-price_size_xs"]/text()').get()      
        question_answered = response.xpath('//div[@class="pdp-review-summary"]/a[2]/text()').get()
        evaluate = response.xpath('//div[@class="pdp-review-summary"]/a/text()').get()
        trademark = response.xpath('//a[@class="pdp-link pdp-link_size_s pdp-link_theme_blue pdp-product-brand__brand-link"]//text()').get()
        sale = response.xpath('//span[2][@class="pdp-product-price__discount"]/text()').get()
        delivery_time = response.xpath('//div[@class="delivery-option-item__time"]/text()').get()
        delivery_charges = response.xpath('//div[@class="delivery-option-item__shipping-fee no-subtitle"]/text()').get()
        payments = response.xpath('//div[@class="delivery-option-item delivery-option-item_type_COD"]/div/div/div/text()').get()
        lie = response.xpath('//div[@class="delivery-option-item delivery-option-item_type_returnPolicy7"]/div/div/div/text()').get()
        insurance = response.xpath('//div[@class="delivery-option-item delivery-option-item_type_noWarranty"]/div/div/div/text()').get()
        shop = response.xpath('//a[@class="pdp-link pdp-link_size_l pdp-link_theme_black seller-name__detail-name"]/text()').get()
        percent_positive_reviews =response.xpath('//div[@class="seller-info-value rating-positive "]/text()').get()
        percentage_of_on_time_delivery = response.xpath('//div[@class="pdp-seller-info-pc"]/div[2]/div[2]//text()').get()
        percent_response_rate = response.xpath('//div[@class="pdp-seller-info-pc"]/div[3]/div[2]/text()').get()
        item= LazadaItem()
        item['name'] = name
        item['sale_price'] = sale_price
        item['initial_price'] = initial_price
        item['question_answered'] = question_answered
        item['evaluate'] = evaluate
        item['trademark'] = trademark
        item['sale'] = sale
        item['delivery_charges'] = delivery_charges
        item['delivery_time'] = delivery_time
        item['payments'] = payments
        item['lie'] = lie
        item['insurance'] = insurance
        item['shop'] = shop
        item['percent_positive_reviews'] = percent_positive_reviews
        item['percentage_of_on_time_delivery'] = percentage_of_on_time_delivery
        item['percent_response_rate'] = percent_response_rate
        yield item
