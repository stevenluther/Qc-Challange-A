import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class Test_search:

    def __init__(self) :
        self.driver = webdriver.Chrome()


    def search(self, term):
        self.driver.get('http://www.google.com')
        self.term = term

        search = self.driver.find_element(By.NAME, "q")

        search.send_keys(term)
        search.send_keys(Keys.RETURN)
        time.sleep(5)
        

    def check_search_result(self):
        search_result = self.driver.find_element(By.NAME, "q").text
        assert search_result == self.term

    def click_first_link(self):
        first_url = self.driver.find_element(By.CSS_SELECTOR,'#rso .g a')
        first_url.click()
        assert self.driver.current_url == 'https://www.facebook.com/'
        
        # If we reach this line it means that all assertions goes as expected and there is no exceptions
        print("Everything goes as expected")

    
if __name__ == "__main__":
    test = Test_search()
    test.search("facebook")
    test.check_search_result()
    test.click_first_link()

