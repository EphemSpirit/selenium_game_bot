from selenium import webdriver
from selenium.webdriver.common.by import By

# Keep chrome open when done
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
# driver.get("https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1")
driver.get("https://www.python.org")

# price_dollar = driver.find_element(By.CLASS_NAME, value="a-price-whole")
# price_cents = driver.find_element(By.CLASS_NAME, value="a-price-fraction")
#
# print(f"Price is {price_dollar.text}.{price_cents.text}")

# search_bar = driver.find_element(By.NAME, value="q")
# print(search_bar.get_attribute("placeholder"))
# submit_button = driver.find_element(By.ID, value="submit")
# print(submit_button.size)
# doc_link = driver.find_element(By.CSS_SELECTOR, value=".documentation-widget a")
# print(doc_link.text)

# bug_submit_link = driver.find_element(By.XPATH, value="/html/body/div/footer/div[2]/div/ul/li[3]/a")
# print(bug_submit_link.text)

dates = driver.find_elements(By.CSS_SELECTOR, value=".event-widget ul time")
dates = [date.text for date in dates]

events = driver.find_elements(By.CSS_SELECTOR, value=".event-widget ul a")
events = [event.text for event in events]

result = dict(zip(dates, events))
print(result)

# close active tab
# driver.close()
# close the whole browser
driver.quit()