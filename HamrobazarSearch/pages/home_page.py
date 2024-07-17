from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, ElementNotInteractableException
from pages.base_page import BasePage
import time

class HomePage(BasePage):
    SEARCH_BOX = (By.XPATH, "//input[@name='searchValue']")
    SEARCH_ICON = (By.XPATH, "//button[@class='nav-searchbar-input-searchIcon']")
    LOCATION_INPUT = (By.XPATH, "//*[@id='hb__root']/div[2]/div[2]/div[1]/aside[2]/div/div[1]/div/form/div[2]/div[2]/div/input")
    LOCATION_OPTION = (By.XPATH, "//strong[text()='naya sadak newroad, New Road, Kathmandu']")
    LOCATION_RADIUS = (By.XPATH, "//*[@id='hb__root']/div[2]/div[2]/div[1]/aside[2]/div/div[1]/div/form/div[2]/div[3]/div/div/div[2]")
    RADIUS_OPTION = (By.XPATH, '//option[@value="5000"]')
    SEARCH_BUTTON = (By.XPATH, "//button[@type='submit']")

    def search_for_monitor(self, searchtext, location):
        # Entering the search text in the search box
        print("Entering search text")
        self.send_keys(*self.SEARCH_BOX, searchtext)

        # Clicking on the search button
        print("Clicking search button")
        self.click(*self.SEARCH_BUTTON)
        time.sleep(5)

        # Entering location in the location input
        print("Entering location")
        self.send_keys(*self.LOCATION_INPUT, location)
        time.sleep(5)

        # Waiting for the dropdown to appear
        print("Selecting location from dropdown")
        self.click(*self.LOCATION_OPTION)
        time.sleep(1)

        # # Selecting the radius option "5000m"
        # print("Selecting radius")
        # self.click(*self.LOCATION_RADIUS)
        # # self.click(*self.RADIUS_OPTION)
        # # time.sleep(2)

        # Clicking search button again to apply filters
        print("Clicking search button again")
        self.click(*self.SEARCH_BUTTON)
        time.sleep(5)
