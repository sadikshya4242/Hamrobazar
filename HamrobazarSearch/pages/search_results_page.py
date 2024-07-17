import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
import pandas as pd

class SearchResultsPage(BasePage):
    SORT_DROPDOWN = (By.XPATH, "//*[@id='hb__root']/div[2]/div[2]/div[1]/aside[2]/div/div[1]/div/form/div[1]/div/select")
    LOW_TO_HIGH_OPTION = (By.XPATH, "//*[@id='hb__root']/div[2]/div[2]/div[1]/aside[2]/div/div[1]/div/form/div[1]/div/select/option[4]")
    ITEM_TITLES = (By.XPATH, "//h2[@class='product-title']")
    ITEM_DESCRIPTIONS = (By.XPATH, "//p[@class='description']")
    ITEM_PRICES = (By.XPATH, "//span[@class='regularPrice']")
    ITEM_CONDITIONS = (By.XPATH, "//span[@class='condition']")
    ITEM_POSTED_DATES = (By.XPATH, "//span[@class='time']")
    ITEM_SELLERS = (By.XPATH, "//span[@class='username-fullname']")

    def sort_by_low_to_high(self):
        self.click(*self.SORT_DROPDOWN)
        time.sleep(2)
        self.click(*self.LOW_TO_HIGH_OPTION)

        # Fetching 5 products details
    def collect_items_details(self):
        titles = [elem.text for elem in self.find_elements(*self.ITEM_TITLES)][:5]
        descriptions = [elem.text for elem in self.find_elements(*self.ITEM_DESCRIPTIONS)][:5]
        prices = [elem.text for elem in self.find_elements(*self.ITEM_PRICES)][:5]
        conditions = [elem.text for elem in self.find_elements(*self.ITEM_CONDITIONS)][:5]
        posted_dates = [elem.text for elem in self.find_elements(*self.ITEM_POSTED_DATES)][:5]
        sellers = [elem.text for elem in self.find_elements(*self.ITEM_SELLERS)][:5]
        return titles, descriptions, prices, conditions, posted_dates,sellers
    # scrolling and fetching product details
    # def collect_items_details(self, num_items=15):
    #     titles = []
    #     descriptions = []
    #     prices = []
    #     conditions =[]
    #     posted_dates =[]
    #     sellers =[]
    #
    #     while len(titles) < num_items:
    #         self.scroll_down()
    #         titles.extend([elem.text for elem in self.find_elements(*self.ITEM_TITLES) if elem.text not in titles])
    #         descriptions.extend([elem.text for elem in self.find_elements(*self.ITEM_DESCRIPTIONS) if elem.text not in descriptions])
    #         prices.extend([elem.text for elem in self.find_elements(*self.ITEM_PRICES) if elem.text not in prices])
    #         conditions.extend([elem.text for elem in self.find_elements(*self.ITEM_PRICES) if elem.text not in prices])
    #         posted_dates.extend([elem.text for elem in self.find_elements(*self.ITEM_PRICES) if elem.text not in prices])
    #         sellers.extend([elem.text for elem in self.find_elements(*self.ITEM_PRICES) if elem.text not in prices])
    #
    #
    #         titles = titles[:num_items]
    #         descriptions = descriptions[:num_items]
    #         prices = prices[:num_items]
    #         conditions = conditions[:num_items]
    #         posted_dates = posted_dates[:num_items]
    #         sellers = sellers[:num_items]
    #
    #     return titles, descriptions, prices, conditions, posted_dates, sellers
    # scrolling the page
    # def scroll_down(self):
    #     self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    #     # Wait for new elements to load
    #     time.sleep(2)

 # Saving the files
    def save_to_csv(self, titles, descriptions, prices, conditions, posted_dates, sellers, filename="Search_Result.csv"):
        data = {
            'Title': titles,
            'Description': descriptions,
            'Price': prices,
            'Condition': conditions,
            'Posted Date': posted_dates,
            'Seller': sellers
        }
        df = pd.DataFrame(data)
        df.to_csv(filename, index=False)
