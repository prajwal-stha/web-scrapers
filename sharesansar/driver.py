from selenium import webdriver
import time
from datetime import date
from selenium.webdriver.common.keys import Keys
from scrape_table_all import scrape_table
from return_dates import return_dates

# Open the link
PATH = "/Users/prajwalshrestha/Desktop/PythonApp/thesis/web-scrapers/sharesansar/chromedriver"
browser = webdriver.Chrome(PATH)
browser.maximize_window()
browser.get("https://www.sharesansar.com/today-share-price")
# Select the type of data to scrape
searchBar = browser.find_element_by_id('sector')
browser.implicitly_wait(20)
# Select Commercial Bank
searchBar.send_keys('Commercial Bank')

sdate = date(2020, 3, 23)
edate = date(2021, 5, 13)
dates = return_dates(sdate, edate)


for day in dates:
    # Enter the date
    date_box = browser.find_elements_by_id('fromdate')
    date_box[0].clear()
    date_box[0].send_keys(day)
    # Click Search
    searchBar = browser.find_element_by_id('btn_todayshareprice_submit')
    searchBar.click()
    time.sleep(3)
    # Needed for this sites
    searchBar.send_keys(Keys.ENTER)
    # Wait for data to show up longer wait time ensures data has loaded before scraping begins
    time.sleep(8)
    # Scrape the table
    html = browser.page_source
    scrape_table(data=html, date=day)

browser.close()
