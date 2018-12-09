from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

driver = webdriver.Chrome("/Users/Dannyniquette/Documents/chromedriver")
driver.get("https://anotherdaywithparadise.herokuapp.com/accounts/signin/")
driver.switch_to_window(driver.current_window_handle)
sleep(4)
username = driver.find_element_by_xpath('//*[@id="id_username"]')
user = "Dniquette"
for i in user:
	username.send_keys(i)
	sleep(0.3)

pword = driver.find_element_by_xpath('//*[@id="id_password"]')
p = "alanparadise"
for j in p:
	pword.send_keys(j)
	sleep(.3)

submit = driver.find_element_by_xpath("/html/body/form/input[4]").click()

business = driver.find_element_by_xpath('//*[@id="home-page"]/div/a[4]').click()

like = driver.find_element_by_xpath('//*[@id="business-page"]/main[2]/article/div/a[1]').click()