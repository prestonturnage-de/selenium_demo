import os
import sys
import traceback

from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


def get_webdriver() -> WebDriver:
    """Retrieve host from environment, initiate, and return the webdriver"""
    host = os.getenv("SELENIUM_HOST", "http://localhost:4444")
    options = webdriver.ChromeOptions()
    options.headless = True
    driver = webdriver.Remote(command_executor=host, options=options)
    return driver


def wait(driver: WebDriver) -> WebDriverWait:
    """Cause the webdriver to wait 5 seconds, because in some cases the docker container is ready before the selenium service is fully up and running"""
    return WebDriverWait(driver=driver, timeout=5)


def main(str_args):
    """Instanciate the selenium webdriver, then use it to run a couple of simple tests.
    Currently, the tests will verify that:
        There are more than 40 records present in the ranks_table
        The elements present in the main-navigation bar match the expected elements
    """
    driver = get_webdriver()
    try:
        url = "https://www.harrisfootball.com/rb-ranks"
        driver.get(url)

        ranks_table = driver.find_elements(By.TAG_NAME, "table")[0]
        ranks = ranks_table.find_elements(By.TAG_NAME, "tr")
        ranks_list = []
        for rank in ranks:
            ranks_list.append([i.text for i in rank.find_elements(By.TAG_NAME, "td")])
        ranks_list = [rank[1].lower().replace(" ", "").replace(".", "").replace("'", "").replace("-", "") for rank in ranks_list[1:-1]]
        print("Testing to ensure that there are at least 40 ranks being displayed...")
        assert len(ranks_list) > 40, "There mustbe at least 40 ranks present here"
        print("Success")

        nav_window = driver.find_element(By.ID, "main-navigation")
        unordered_list = nav_window.find_element(By.TAG_NAME, "ul")
        list_items = unordered_list.find_elements(By.TAG_NAME, "li")

        expected_items = [
            "Home",
            "Podcast",
            "Ranks",
            "Yacht Club Podcast Subscription!",
            "Mixtapes",
            "Pod Sponsors",
            "Advertise",
            "YouTube Channel",
            "Music",
            "About",
            "Get A Novel By Harris",
            "Yacht Club Dictionary",
            "Harris Football Merch",
        ]
        actual_items = [list_item.find_element(By.TAG_NAME, "a").text for list_item in list_items]
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
    """test comment"""
    run()
