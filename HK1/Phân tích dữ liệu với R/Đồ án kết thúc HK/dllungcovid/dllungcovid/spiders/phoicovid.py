import scrapy
from..items import DllungcovidItem
from scrapy_selenium import SeleniumRequest
from selenium import webdriver
from scrapy.utils.project import get_project_settings

class PhoicovidSpider(scrapy.Spider):
    name = 'phoicovid'
    def start_requests(self):
        settings= get_project_settings()
        driver_path = settings['CHROME_DRIVER_PATH']
        options= webdriver.ChromeOptions()
        options.headless = True
        driver = webdriver.Chrome(driver_path, options=options)
        driver.get('https://www.eurorad.org/advanced-search?search=COVID&sort_by=published_at&sort_order=DESC&page=0&filter%5B0%5D=section%3A40&filter%5B1%5D=area_of_interest%3A112')
        link_elements = driver.find_elements_by_xpath(
            '//*[@class="col-12 col-md-6 col-lg-4 mb-4"]//a[text()]'
        )
        for link in link_elements:
            yield scrapy.Request(link.get_attribute('href'), callback=self.parse)
        driver.quit()

    def parse(self, response):
        if response.xpath('//div[@class="col-12 col-lg-8"]').get() is not None: 
            stt = response.xpath('//span[@class="d-block text-uppercase font-size-3 text-center"]/text()').get()
            ngay_thang_nam = response.xpath('//span[@class="d-block font-size-1 text-center"]/text()').get()
            tieu_de = response.xpath('//h1[@class="color-color mb-3"]/text()').get()
            the_loai = response.xpath('//div[@class="col-12 order-0 col-md-8 order-md-1 col-lg-9 mb-3"]/div/div/p/text()').get()
            loai_truong_hop = response.xpath('//div[@class="col-12 order-0 col-md-8 order-md-1 col-lg-9 mb-3"]/div/div/p[2]/text()').get()
            cac_tac_gia = response.xpath('//div[@class="col-12 order-0 col-md-8 order-md-1 col-lg-9 mb-3"]/div/div/p[4]/text()').get()
            tuoi_va_gioi_tinh = response.xpath('//p[@class="color-grey"]/text()').get()
            lich_su_lam_sang = {response.xpath('//div[@class="block__content node-contents"]/div/div/div[2]/p/span/span/span/text()').get(),
                                    response.xpath('//div[@class="block__content node-contents"]/div/div/div[2]/p/span/span/span/span[3]/text()').get(),
                                    response.xpath('//div[@class="block__content node-contents"]/div/div/div[2]/p/span/span/span/span/span/span/text()').get()}  
            ket_qua_hinh_anh = {response.xpath('//div[@class="block__content node-contents"]/div[2]/div/div[2]/p/span/span/span/text()').get(),
                                    response.xpath('//div[@class="block__content node-contents"]/div[2]/div/div[2]/p/span/span/span/span/span/span/text()').get(),
                                    response.xpath('//div[@class="block__content node-contents"]/div[2]/div/div[2]/p/span/span/span/span[3]/text()').get(),
                                    response.xpath('//div[@class="block__content node-contents"]/div[2]/div/div[2]/p/span/text()').get(),
                                    response.xpath('//div[@class="block__content node-contents"]/div[2]/div/div[2]/p/span/span/span/span[3]/span/text()').get()}
            thao_luan_tieu_su = {response.xpath('//div[@class="block__content node-contents"]/div[3]/div/div[2]/p[2]/span/span/span/text()').get(),
                                    response.xpath('//div[@class="block__content node-contents"]/div[3]/div/div[2]/p[2]/span/span/span/span/span/span/text()').get(),
                                    response.xpath('//div[@class="block__content node-contents"]/div[3]/div/div[2]/p[2]/span/span/span/span/span/text()').get(),
                                    response.xpath('//div[@class="block__content node-contents"]/div[3]/div/div[2]/p[2]/span/text()').get(),
                                    response.xpath('//div[@class="block__content node-contents"]/div[3]/div/div[2]/p/span/span/span/span/text()').get(),
                                    response.xpath('//div[@class="block__content node-contents"]/div[3]/div/div[2]/p[3]/span/span/span/span/span/span/span/text()').get()}
            thao_luan_quan_diem_lam_sang = {response.xpath('//div[@class="block__content node-contents"]/div[3]/div/div[2]/p[5]/span/span/span/span/text()').get(),
                                                response.xpath('//div[@class="block__content node-contents"]/div[3]/div/div[2]/p[5]/span/span/span/span/span/text()').get(),
                                                response.xpath('//div[@class="block__content node-contents"]/div[3]/div/div[2]/p[2]/span/span/span/span[2]/text()').get(),
                                                response.xpath('//div[@class="block__content node-contents"]/div[3]/div/div[2]/p[7]/span/span/span/span/span/span/text()').get(),
                                                response.xpath('//div[@class="block__content node-contents"]/div[3]/div/div[2]/p[3]/span/span/span/text()').get()}                                
            thao_luan_phoi_canh_hinh_anh = {response.xpath('//div[@class="block__content node-contents"]/div[3]/div/div[2]/p[9]/span/span/span/span[4]/text()').get(),
                                                response.xpath('//div[@class="block__content node-contents"]/div[3]/div/div[2]/p[6]/span/span/span/text()').get(),
                                                response.xpath('//div[@class="block__content node-contents"]/div[3]/div/div[2]/p[7]/span/span/text()').get(),
                                                response.xpath('//div[@class="block__content node-contents"]/div[2]/div/div[2]/p[3]/span/span/span/span/span/span/text()').get(),
                                                response.xpath('//div[@class="block__content node-contents"]/div[3]/div/div[2]/p[9]/span/span/span/span/span/span/span/text()').get(),
                                                response.xpath('//div[@class="block__content node-contents"]/div[3]/div/div[2]/p[6]/span/span/span/span/span/text()').get(),
                                                response.xpath('//div[@class="block__content node-contents"]/div[3]/div/div[2]/p[4]/span/span/span/text()').get()}
            thao_luan_ket_qua = {response.xpath('//div[@class="block__content node-contents"]/div[3]/div/div[2]/p[11]/span/span/span/text()').get(),
                                    response.xpath('//div[@class="block__content node-contents"]/div[3]/div/div[2]/p[11]/span/span/span/span/text()').get(),
                                    response.xpath('//div[@class="block__content node-contents"]/div[3]/div/div[2]/p[11]/span/span/span/span/span/span/text()').get(),
                                    response.xpath('//div[@class="block__content node-contents"]/div[3]/div/div[2]/p[13]/span/span/span/span/span/span/span/text()').get(),
                                    response.xpath('//div[@class="block__content node-contents"]/div[3]/div/div[2]/p[8]/span/span/span/span/span/text()').get(),
                                    response.xpath('//div[@class="block__content node-contents"]/div[3]/div/div[2]/p[8]/span/span/span/span/span/span/text()').get(),
                                    response.xpath('//div[@class="block__content node-contents"]/div[3]/div/div[2]/p[8]/span/span/text()').get(),
                                    response.xpath('//div[@class="block__content node-contents"]/div[3]/div/div[2]/p[6]/span/span/span/text()').get(),
                                    response.xpath('//div[@class="block__content node-contents"]/div[3]/div/div[2]/p[5]/span/text()').get()}                                 
            danh_sach_chuan_doan = {response.xpath('//div[@class="col-6 pb-3"]/text()').get(),
                                        response.xpath('//div[3][@class="col-6 pb-3"]/text()').get(),
                                        response.xpath('//div[5][@class="col-6 pb-3"]/text()').get(),
                                        response.xpath('//div[2][@class="col-6 pb-3"]/text()').get(),
                                        response.xpath('//div[4][@class="col-6 pb-3"]/text()').get(),
                                        response.xpath('//div[6][@class="col-6 pb-3"]/text()').get()}
            chuan_doan_cuoi = response.xpath('//div[@class="block__content node-contents"]/div[5]/div/div[2]/text()').get()  
            ten_anh = response.xpath('//div[@class="figure-gallery__item__label"]/span/text()').get()           
            item = DllungcovidItem()
            item["stt"] = stt
            item["ngay_thang_nam"] = ngay_thang_nam
            item["tieu_de"] = tieu_de
            item["the_loai"] = the_loai
            item["loai_truong_hop"] = loai_truong_hop
            item["cac_tac_gia"] = cac_tac_gia
            item["tuoi_va_gioi_tinh"] = tuoi_va_gioi_tinh
            item["lich_su_lam_sang"] = lich_su_lam_sang
            item["ket_qua_hinh_anh"] = ket_qua_hinh_anh
            item["thao_luan_tieu_su"] = thao_luan_tieu_su
            item["thao_luan_quan_diem_lam_sang"] =  thao_luan_quan_diem_lam_sang
            item["thao_luan_phoi_canh_hinh_anh"] =  thao_luan_phoi_canh_hinh_anh
            item["thao_luan_ket_qua"] = thao_luan_ket_qua
            item["danh_sach_chuan_doan"] = danh_sach_chuan_doan
            item["chuan_doan_cuoi"] = chuan_doan_cuoi
            item["ten_anh"] = ten_anh
            yield item
            pass