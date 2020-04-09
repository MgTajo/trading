from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.get("https://www.coindesk.com/price/bitcoin")
sleep(4)
# cookies_bitcoin = driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[5]/div[1]/a").click()
price_last = 0
current_high = 0
while True:
    sleep(3)
    price = driver.find_element_by_xpath(
        "/html/body/div/main/section/div/div[1]/div/section/div/div/section[1]/div/dl[1]/dd").text
    price_float = str(price[1:3]) + str(price[4:])
    print(price_float)
    driver.refresh()

