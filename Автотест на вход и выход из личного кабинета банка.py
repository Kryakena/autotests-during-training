from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

s=Service('C:/Users/Kryakena/Downloads/chromedriver-win64/chromedriver.exe')
driver = webdriver.Chrome(service=s)
driver.get("https://idemo.bspb.ru/auth?response_type=code&client_id=1&redirect_uri=https%3A%2F%2Fidemo.bspb.ru%2Flogin%2Fsuccess&prefetch_uri=https%3A%2F%2Fidemo.bspb.ru%2Flogin%2Fprefetch&force_new_session=true")
time.sleep(5)
driver.set_window_size(1366,768)
driver.find_element(By.NAME, "username").clear()
driver.find_element(By.NAME, "username").send_keys("demo")
driver.find_element(By.NAME, "password").clear()
driver.find_element(By.NAME, "password").send_keys("demo")
driver.find_element(By.ID, "login-button").click()
time.sleep(3)
driver.find_element(By.ID, "otp-code").clear()
driver.find_element(By.ID, "otp-code").send_keys("0000")
driver.find_element(By.ID, "login-otp-button").click()
time.sleep(3)
driver.find_element(By.ID,"logout-button").click()
time.sleep(5)