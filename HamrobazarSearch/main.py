import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from pages.home_page import HomePage
from pages.search_results_page import SearchResultsPage

def main():
    # Using drivermanager to automatically download the chrome driver
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    try:

        home_page = HomePage(driver)
        search_results_page = SearchResultsPage(driver)

        # Opening Hamrobazar
        home_page.open_url("https://hamrobazar.com")
        driver.maximize_window()
        print("Opened Hamrobazar")

        # Waiting for the page to load
        time.sleep(2)

        # Performing a search for "Monitor" and location "New Road"
        home_page.search_for_monitor("Monitor", "New Road")
        print("Performed search for Monitor")

        # Waiting for the search results to load
        time.sleep(2)

        # Sorting results by Low to High Price
        search_results_page.sort_by_low_to_high()
        print("Sorted results by price")

        # Waiting for sorting to complete
        time.sleep(5)

        # Collecting details of top 5 items
        titles, descriptions, prices, conditions, posted_dates, sellers = search_results_page.collect_items_details()

        # Saving details to a CSV file
        search_results_page.save_to_csv(titles, descriptions, prices, conditions, posted_dates, sellers)
        print("Saved results to Search_Result.csv")

        # Displaying the data in tabular format
        df = pd.read_csv("Search_Result.csv")
        print(df)

    finally:
        # Quiting the driver
        driver.quit()

if __name__ == "__main__":
    main()
