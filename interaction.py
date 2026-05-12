from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome()

driver.get("https://en.wikipedia.org/wiki/Main_Page")

english_article_count = driver.find_element(By.XPATH, value="/html/body/div[3]/div/div[3]/main/div[3]/div[3]/div[2]/div[1]/div/div[3]/ul/li[2]/a[1]")
print(english_article_count.text)