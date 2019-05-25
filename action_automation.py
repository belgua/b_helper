from selenium import webdriver
import time
from getpass import getuser
class action_interface:

    def __init__ (self):
        self.action()

    def action(self):
        # Chrome driver path
        chromedriver = r"C:\Users\Borat\Desktop\chromedriver.exe"

        # Get chrome options
        chrome_options = webdriver.ChromeOptions()

        # Load current user default profile
        current_user = getuser()
        chrome_options.add_argument(r"--user-data-dir=C:\Users\{}\AppData\Local\Google\Chrome\User Data".format(current_user))

        # didable "Chrome is being controled by an automated test software"
        chrome_options.add_argument('disable-infobars')

        # get Chrome to stay open
        chrome_options.add_experimental_option("detach", True)

        # open browser with options and driver
        my_driver = webdriver.Chrome(options=chrome_options,executable_path=chromedriver)

        # Open site
        my_driver.get('https://www.youtube.com/watch?v=y3O3xSg_AIo&list=RD5WEggKymynE&index=9')

        # get element and click
        button = my_driver.find_element_by_class_name("style-scope yt-icon")
        button.click()

if __name__ == "__main__":
    AI = action_interface()