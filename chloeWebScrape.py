'''
File name:   chloeWebScrape.py
Author:      Charlie Kelley
Date:        22-Feb-2021
'''

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time

class Votebot():
  def __init__(self):
    self.chromePath = "C:\webdrivers\chromedriver.exe"
    capabilities = DesiredCapabilities.CHROME.copy()
    capabilities['platform'] = "WINDOWS"
    capabilities['version'] = "10"
    self.browser = webdriver.Chrome(executable_path=self.chromePath, desired_capabilities=capabilities)
    self.url = 'https://www.newsobserver.com/sports/high-school/article249416675.html'
    # self.url = 'https://www.youtube.com')
    self.browser.get(self.url)

    # chloeOption = self.browser.find_element_by_id("PDI_answer49662231")
    # self.browser.execute_script("arguments[0].click();", chloeOption
    # submitButton = self.browser.find_element_by_id("pd-vote-button10752408")

    chloeOption = WebDriverWait(self.browser, 10).until(lambda x: x.find_element_by_id("PDI_answer49662231"))
    self.browser.execute_script("arguments[0].click();", chloeOption)

    is_clicked = chloeOption.get_attribute("checked")
    while not is_clicked:
      is_clicked = chloeOption.get_attribute("checked")


    submitButton = WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable((By.ID, "pd-vote-button10752408")))
    self.browser.execute_script("arguments[0].click();", submitButton)

    submitButton = WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable((By.ID, "pd-vote-button10752408")))
    self.browser.execute_script("arguments[0].click();", submitButton)

    submitButton = WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable((By.ID, "pd-vote-button10752408")))
    self.browser.execute_script("arguments[0].click();", submitButton)


if __name__ == "__main__":

  bot = Votebot()
  time.sleep(5)
  bot.browser.close()

