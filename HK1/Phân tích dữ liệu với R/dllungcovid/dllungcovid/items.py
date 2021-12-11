# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class DllungcovidItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    stt = scrapy.Field()
    ngay_thang_nam = scrapy.Field()
    tieu_de = scrapy.Field()
    the_loai = scrapy.Field()
    loai_truong_hop = scrapy.Field()
    cac_tac_gia = scrapy.Field()
    tuoi_va_gioi_tinh = scrapy.Field()
    lich_su_lam_sang = scrapy.Field()
    ket_qua_hinh_anh = scrapy.Field()
    thao_luan_tieu_su = scrapy.Field()
    thao_luan_quan_diem_lam_sang = scrapy.Field()
    thao_luan_phoi_canh_hinh_anh = scrapy.Field()
    thao_luan_ket_qua = scrapy.Field()
    danh_sach_chuan_doan = scrapy.Field()
    chuan_doan_cuoi = scrapy.Field()
    ten_anh = scrapy.Field()
    pass
