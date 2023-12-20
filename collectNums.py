"""
File collects numbers from website and stores them in files
Start date for RnG in power 1st July 2017
"""


import time
import sys

import selenium.common.exceptions
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ChromeOptions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CollectNums:
    def __init__(self, url, file):
        self.currentPosition = None
        options = ChromeOptions()
        options.headless = True
        self.driver = webdriver.Chrome()
        self.driver.get(url)
        self.driver.implicitly_wait(10)
        self.file_name = file
        self.file = open(file + '.txt', 'w')
        self.period = time.sleep
        self.wait = WebDriverWait(self.driver, 10)
        self.date = time.asctime().split(' ')[3]
        self.pageNumber = 1

    def add_nums(self):
        """
        Add numbers to draws by scrapping  new results.
        """
        self.driver.find_element(By.XPATH, '//input[@id="fromDate"]').click()  # click calender
        self.driver.find_element(By.XPATH, '//td[@class="day" and text()="7"]').click()  # select start date

        # Select second date
        self.driver.find_element(By.XPATH, '//input[@type="text" and @id="toDate"]').click()
        day = int(self.date) - 1
        self.driver.find_element(By.XPATH,
                                 f'//td[@class="day" and text() ="{day}"]').click()
        self.driver.find_element(By.XPATH, '//div[@class="btnBox" and text() ="Search"]').click()  # Search

    def selectDate(self):
        """
        select date range from 17 may to 4 july 2017
        """
        self.driver.find_element(By.XPATH, '//input[@id="fromDate"]').click()    # click calender
        self.driver.find_element(By.XPATH, '//th[text()="November 2022"]').click()    # select first month
        self.driver.find_element(
            By.XPATH, '//th[@class="datepicker-switch" and text()="2022"]').click()    # select year

        allClicks = self.driver.find_elements(By.XPATH, '//th[@style="visibility: visible;" and @class="prev"]')
        print(len(allClicks))
        allClicks[2].click()

        self.driver.find_element(By.XPATH, '//span[@class="year" and  text()=2017]').click()
        self.driver.find_element(By.XPATH, '//span[text()="Mar" and @class="month"]').click()
        self.driver.find_element(By.XPATH, '//td[@class="day" and text()="4"]').click()
        self.driver.find_element(By.XPATH, '//input[@type="text" and @id="toDate"]').click()
        day = int(self.date) - 1
        self.driver.find_element(By.XPATH, f'//td[@class="day" and text() ="{day}"]').click()
        self.driver.find_element(By.XPATH, '//div[@class="btnBox" and text() ="Search"]').click() # Search

    def flip_page(self):
        # Flip from one page to the next
        try:
            if self.pageNumber % 5 == 0:
                self.driver.find_element(By.XPATH, '//i[@class="fa fa-angle-right"]').click() # or use '//i[@class="fa fa-bars"]'
                self.pageNumber += 1
                self.period(3)
                print(self.pageNumber, "PAGE")
            else:
                self.wait.until(EC.element_to_be_clickable((By.XPATH, '//i[@class="fa fa-angle-right"]')))
                self.driver.find_element(By.XPATH, '//i[@class="fa fa-angle-right"]').click()  # or use '//i[@class="fa fa-bars"]'
                self.pageNumber += 1
        except:
            self.wait.until(EC.element_to_be_clickable((By.XPATH, '//i[@class="fa fa-angle-right"]')))
            self.driver.find_element(By.XPATH, '//i[@class="fa fa-angle-right"]').click()  # or use '//i[@class="fa fa-bars"]'
            self.pageNumber += 1

    def copy_numbers(self):
        # copy numbers to text files
        self.wait.until(EC.presence_of_element_located((By.XPATH, '//div[@class="shape"]')))
        names = self.driver.find_elements(By.XPATH, '//div[@class="shape"]')
        if self.file_name == 'daily':
            cut = 5
        elif self.file_name == ('plus' or 'power'):
            cut = 6
        else:
            cut = 7

        hold = []
        for item in names:
            if len(hold) == cut:
                self.file.writelines(f'{hold} \n')
                hold = []
            try:
                if item.text == '':
                    continue
                hold.append(item.text)
            except selenium.common.exceptions.StaleElementReferenceException:
                pass
        print("Done")

    def adder(self):
        # add numbers to text files
        self.add_nums()
        while True:
            try:
                self.copy_numbers()
            except:
                return

    def runner(self):
        # Collect numbers
        self.selectDate()
        for _ in range(61):
            try:
                self.copy_numbers()
            except:
                return
            self.flip_page()


urls = [('https://www.nationallottery.co.za/daily-lotto-history', 'daily'),]

#
for x, y in urls:
    draws = CollectNums(x, y)
    draws.add_nums()
