from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os





if __name__ == '__main__':
    options = Options()
    options.binary_location = '/Applications/Brave Browser.app/Contents/MacOS/Brave Browser'
    cwd = os.getcwd()
    chromium_driver = 'drivers/chromedriver'
    driver = webdriver.Chrome(options = options, executable_path = os.path.join(cwd, chromium_driver))
    driver.get('https://www.wokin.cz/')

    # objednat online button
    order_btn = driver.find_element_by_xpath('//*[@id="collapsingNavbar"]/ul/li[4]/a')
    order_btn.click()

    # select the branch
    branch_select_btn = driver.find_element_by_xpath('//*[@id="branchOuter"]/div/div[1]')
    branch_select_btn.click()

    # get Jindrisska
    branch_btn = driver.find_element_by_xpath('//*[@id="branchOuter"]/div/div[2]/div[1]')
    branch_btn.click()

    #driver.close()
