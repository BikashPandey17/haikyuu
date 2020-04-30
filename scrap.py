from selenium_wrapper import SeleniumBrowser
import time

def main():
    sbo = SeleniumBrowser()
    browser = sbo.connect('https://haikyu-top.com/manga/haikyuu-chapter-391/')

    # sleep for some time after opening the browser
    time.sleep(5)
    SCROLL_PAUSE_TIME = 0.5

    i = 0
    for i in range(0,41):
        # Scroll down to bottom
        browser.save_screenshot("data/english/screenshot{}.png".format(i))
        browser.execute_script("window.scrollTo(0, window.scrollY + 400)")
        # .format(1070*(i+1))
        # Wait to load page
        time.sleep(SCROLL_PAUSE_TIME)
    
    sbo.stop_selenium()

    return 1

main()