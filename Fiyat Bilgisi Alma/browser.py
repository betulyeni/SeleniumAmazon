from selenium import webdriver
import time

class Browser:
    def __init_( self, time, count, link):
        driver_Path="C:\Users\betul\OneDrive\Belgeler\GitHub\amazon\chromedriver.exe"
        self.browser=webdriver.chrome(driver_Path)
        self.time = time
        self.count = count
        self.link = link
        Browser.goAmazon(self)
    def goAmazon(self):
        self.browser.get(self.link)
        Browser.checkPrice(self)
    def checkPrice(self):
        for x in range(0, self.conut, 1):
            price = self.browser.find_element_by_id('price_inside_buybox').text
            print(price)
            time.sleep(self.time)
            self.browser.quit()
