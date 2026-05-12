from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

# driver.get("https://en.wikipedia.org/wiki/Main_Page")
driver.get("https://secure-retreat-92358.herokuapp.com/")

# english_article_count = driver.find_element(By.XPATH, value="/html/body/div[3]/div/div[3]/main/div[3]/div[3]/div[2]/div[1]/div/div[3]/ul/li[2]/a[1]")
#
# # english_article_count.click()
# all_portals = driver.find_element(By.LINK_TEXT, value="Content portals")
# # all_portals.click()
#
# # search_box = driver.find_element(By.NAME, value="search")
# search_box = WebDriverWait(driver, 10).until(
#     EC.element_to_be_clickable((By.NAME, "search"))
# )
#
# search_box.send_keys("Python", Keys.ENTER)
first_name = driver.find_element(By.NAME, value="fName")
first_name.send_keys("fewhff")

last_name = driver.find_element(By.NAME, value="lName")
last_name.send_keys("hoiubniub")

email = driver.find_element(By.NAME, value="email")
email.send_keys("fhewoif@ho.com")

submit_btn = driver.find_element(By.CSS_SELECTOR, value="form button")
submit_btn.click()
