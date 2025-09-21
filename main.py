from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import traceback
from frequency import frequency as base_frequency
from collections import Counter
from string import ascii_lowercase
from math import sqrt
from time import sleep
import sys
import os

def get_webdriver() -> WebDriver:
    host = os.getenv("SELENIUM_HOST", "http://localhost:4444")
    options = webdriver.ChromeOptions()
    options.headless = True
    driver = webdriver.Remote(command_executor=host, options = options)
    return driver

def wait(driver:WebDriver) -> WebDriverWait:
    return WebDriverWait(driver=driver, timeout=5)

def main(str_args):
    driver = get_webdriver()
    try:
        url="https://www.harrisfootball.com/rb-ranks"
        driver.get(url)

        ranks_table_div = driver.find_element(By.ID, "Ranks Staging_6459")
        ranks_table = driver.find_elements(By.TAG_NAME, "table")[0]
        ranks = ranks_table.find_elements(By.TAG_NAME, "tr")
        ranks_list = []
        for rank in ranks:
            ranks_list.append([i.text for i in rank.find_elements(By.TAG_NAME, "td")])
        ranks_list = [rank[1].lower().replace(" ", "").replace(".", "").replace("'", "").replace("-", "") for rank in ranks_list[1:-1]]
        print("Testing to ensure that there are at least 40 ranks being displayed...")
        assert len(ranks_list) > 40, "There mustbe at least 40 ranks present here"
        print("Success")

        """
        all_names = "".join(ranks_list)
        letter_counts = Counter(all_names)
        letter_frequency_in_names = {key: value/len(all_names) for key, value in letter_counts.items()}
        squared_distance = 0
        for letter in ascii_lowercase:
            squared_distance += (letter_frequency_in_names.get(letter, 0) - base_frequency[letter])**2
        distance = sqrt(squared_distance)
        """
        
        nav_window = driver.find_element(By.ID, "main-navigation")
        unordered_list = nav_window.find_element(By.TAG_NAME, 'ul')
        list_items = unordered_list.find_elements(By.TAG_NAME, "li")

        expected_items = ["Home", "Podcast", "Ranks", "Yacht Club Podcast Subscription!", "Mixtapes", "Pod Sponsors", "Advertise", "YouTube Channel", "Music",
                "About", "Get A Novel By Harris", "Yacht Club Dictionary", "Harris Football Merch"]
        actual_items = [list_item.find_element(By.TAG_NAME, 'a').text for list_item in list_items]
        print("Checking that main nav bar matches expected values...")
        assert set([i.upper() for i in expected_items]) == set([i.upper() for i in actual_items])
        print("Success")
        
        driver.quit()
    except Exception as e:
        traceback.print_exc()
        print(e)
        driver.quit()

def run():
    main(sys.argv[1:])

if __name__ == "__main__":
    run()
    """
    find freq for each letter in names 
    hard code freq of letters in english (dict)
    find cartesian distance between frequencies
    d = sqrt((a1- a2)^2 + (b1 - b2)^2... (z1- z2)^2)
    a1 = source frequency (from player names)
    a2 = ref frequency (from hard coded dictionary)
    """
