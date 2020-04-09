class read_in:
    from selenium import webdriver
    from time import sleep
    driver = webdriver.Chrome()
    driver.get("https://www.coindesk.com/price/bitcoin")
    sleep(4)
    #cookies_bitcoin = driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[5]/div[1]/a").click()
    price_last = 0
    current_high = 0
    while True:
        sleep(3)
        price = driver.find_element_by_xpath(
            "/html/body/div/main/section/div/div[1]/div/section/div/div/section[1]/div/dl[1]/dd").text
        price_float = str(price[1:3]) + str(price[4:])
        price = price[1:]
        change = driver.find_element_by_xpath(
            "/html/body/div/main/section/div/div[1]/div/section/div/div/section[1]/div/dl[2]/dd/span/span/span[1]").text
        change_second = (float(price_last) / float(price_float)) / 100
        if float(price_last) == float(price_float):
            change_second = 0.0000
        if float(price_last) > float(price_float):
            change_second = 0 - change_second
        absolute_change = float(price_float) - float(price_last)
        absolute_change = str(absolute_change)
        change_second = str(change_second)
        print("Current Bitcoin price: ", price, "        Change in the last 24h:", change, "%",
              "        Absolut change: ", absolute_change[:5],
              "$", "        Change in last second: ", change_second[:6], "%", "        Current High: ", current_high, "$")
        price_last = price_float
        driver.refresh()
        if float(price_float) > current_high:
            current_high = float(price_float)










