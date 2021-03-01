from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

import pandas as pd

def Database(Companies):
    driver = webdriver.Chrome()
    driver.maximize_window()

    for company in Companies:
        driver.get("https://in.finance.yahoo.com/")
        driver.find_element_by_id("yfin-usr-qry").send_keys(company)
        driver.find_element_by_id("search-button").click()
        time.sleep(5)

        driver.find_element_by_xpath('''//*[@id="quote-nav"]/ul/li[5]/a''').click()
        time.sleep(5)

        driver.find_element_by_xpath('''//*[@id="Col1-1-HistoricalDataTable-Proxy"]/section/div[1]/div[1]/div[1]/div/div/div/span''').click()
        driver.find_element_by_xpath('''//*[@id="dropdown-menu"]/div/ul[2]/li[4]/button''').click()
        driver.find_element_by_xpath('''//*[@id="Col1-1-HistoricalDataTable-Proxy"]/section/div[1]/div[1]/button''').click()

        # Scrolls the Webpage
        i = 1
        while(i < 100):
            driver.execute_script(f"window.scrollTo(0, (document.body.scrollHeight)*{i * 10});")
            i = i + 1
            time.sleep(0.5)

        # Pulls the Historical Data
        data = []
        webpage = driver.page_source
        soup = BeautifulSoup(webpage, 'lxml')
        stock_prices = soup.find_all('tr', class_='BdT Bdc($seperatorColor) Ta(end) Fz(s) Whs(nw)')
        for stock_price in stock_prices:
            stock_price = stock_price.find_all('td')
            price = []
            for stock in stock_price:
                price.append(stock.text)
            data.append(price)

        # Generate csv file 
        database = pd.DataFrame(data, columns = ["Date", "Open", "High", "Low", "Close", "Adj. Close", "Volume"])
        database.to_csv(rf'Database\{company}.csv', index = False)
    
    driver.quit()

if __name__ == "__main__":
    List_of_Companies = ['GOOG', 'AAPL', 'MSFT', 'TSLA', 'AMZN']
    Database(List_of_Companies)