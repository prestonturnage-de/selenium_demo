from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import traceback

DRIVER_URL = "http://localhost:4444"

def get_webdriver() -> WebDriver:
    options = webdriver.ChromeOptions()
    options.headless = True

    driver = webdriver.Remote(command_executor=DRIVER_URL, options = options)
#    driver.set_script_timeout(30)
#    driver.set_page_load_timeout(30)

    return driver

def wait(driver:WebDriver) -> WebDriverWait:

    return WebDriverWait(driver=driver, timeout=5)

def main():
    driver = get_webdriver()
    try:
        url="https://www.harrisfootball.com/rb-ranks"

        elements = ["Home", "Podcast", "Ranks", "Yacht Club Podcast Subscription!", "Mixtapes", "Pod Sponsors", "Advertise", "YouTube Channel", "Music",
                "About", "Get A Novel By Harris", "Yacht Club Dictionary", "Harris Football Merch"]

        driver.get(url)
        ranks_table_div = driver.find_element(By.ID, "Ranks Staging_6459")
        ranks_table = driver.find_elements(By.TAG_NAME, "table")[0]
        ranks = ranks_table.find_elements(By.TAG_NAME, "tr")
#        print(ranks)
        ranks_list = []
        for rank in ranks:
            ranks_list.append([i.text for i in rank.find_elements(By.TAG_NAME, "td")])
        for i,j in enumerate(ranks_list):
            print(i,':',j)
        
        """
        nav_window = driver.find_element(By.ID, "main-navigation")
        print(nav_window)
        list_items = nav_window.find_elements(By.TAG_NAME, "li")
        print(list_items)
        """
        driver.quit()
    except Exception as e:
        traceback.print_exc()
        print(e)
        driver.quit()

if __name__ == "__main__":
    main()
    """
    find freq for each letter in names 
    hard code freq of letters in english (dict)
    find cartesian distance between frequencies
    d = sqrt((a1- a2)^2 + (b1 - b2)^2... (z1- z2)^2)
    a1 = source frequency (from player names)
    a2 = ref frequency (from hard coded dictionary)
    """
