class trade:
    from selenium import webdriver
    from time import sleep
    email = "spampi31415926@gmail.com"
    pw = "0038a7b11XWB"
    driver = webdriver.Chrome()
    driver.get("https://www.nextmarkets.com/de/handeln")
    sleep(3)
    login_field = driver.find_element_by_xpath(
        "/html/body/nm-app/nm-loader/nm-modal[1]/div/div[2]/nm-login/div/form/div[1]/fieldset/input").send_keys(
        email)
    pw_filed = driver.find_element_by_xpath(
        "/html/body/nm-app/nm-loader/nm-modal[1]/div/div[2]/nm-login/div/form/div[2]/fieldset/input").send_keys(pw)
    button = driver.find_element_by_xpath(
        "/html/body/nm-app/nm-loader/nm-modal[1]/div/div[2]/nm-login/div/form/fieldset/button").click()
    sleep(4)
    cookies = driver.find_element_by_xpath(
        "/html/body/nm-app/nm-loader/nm-cookie-dialog/nm-lightbox/div/div[2]/div[2]/a").click()
    sleep(1)
    echtgeld = driver.find_element_by_xpath("/html/body/nm-account-info-switch/div/div/span").click()
    sleep(1)
    menue = driver.find_element_by_xpath(
        "/html/body/nm-app/div[1]/main/article/div/div[1]/das-chart/div[1]/ul/li[1]/span[1]").click()
    sleep(1)
    bitcoin = driver.find_element_by_xpath(
        "/html/body/nm-app/div[1]/main/article/div/div[1]/das-chart/div[1]/ul/li[1]/div/div/div/nm-watchlist/div/div/ul/li[5]/div/a").click()