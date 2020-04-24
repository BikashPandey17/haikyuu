from bs4 import BeautifulSoup as bs
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager


SELENIUM_EXTENSION = 'F:\\downloads_oct_26\\chrome_driver\\1.22.2_0'

class SeleniumBrowser():

    def __init_selenium(self):
        try:
            options = webdriver.ChromeOptions()
            options.add_argument('--ignore-certificate-errors')
            options.add_argument('--incognito')
            # options.add_argument('--headless')
            options.add_argument('load-extension=' + SELENIUM_EXTENSION)
            browser = webdriver.Chrome(
                ChromeDriverManager().install(), options=options)
            return browser
        except:
            raise
            

    def __init__(self):
        # self.collector, _ = gen_collection(uid)
        self.browser = self.__init_selenium()

    def __restart_selenium(self):
        self.browser.close()
        self.browser = self.__init_selenium()

    def __check_browser_connect(self, browser):
        """
        Checks if the browsers connection is correct or not
        """
        text = browser.text
        print(text)
        messages = ["might be temporarily down or it may have moved permanently to a new web address",
                    "There is something wrong with the proxy server, or the address is incorrect."]
        return True

    def stop_selenium(self):
        self.browser.close()

    def connect(self, link, number_of_retries=3):
        browser = self.browser
        # browser = init_selenium(proxy.host + ":" + proxy.port)
        while number_of_retries:
            # Loop till a valid hit
            try:
                browser.get(link)
                # check if it returns correctly
                # if not check_browser_connect(browser):
                #     raise
                return browser
            except:
                self.__restart_selenium()
                number_of_retries -= 1
                continue
        # browser.close()
        return False


