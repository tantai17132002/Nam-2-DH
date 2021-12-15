# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class LazadaItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.Field()
    sale_price = scrapy.Field()
    initial_price = scrapy.Field()
    question_answered = scrapy.Field()
    evaluate = scrapy.Field()
    trademark = scrapy.Field()
    sale = scrapy.Field()
    delivery_charges = scrapy.Field()
    delivery_time = scrapy.Field()
    payments = scrapy.Field()
    lie = scrapy.Field()
    insurance = scrapy.Field()
    shop = scrapy.Field()
    percent_positive_reviews = scrapy.Field()
    percentage_of_on_time_delivery = scrapy.Field()
    percent_response_rate = scrapy.Field()
    pass
