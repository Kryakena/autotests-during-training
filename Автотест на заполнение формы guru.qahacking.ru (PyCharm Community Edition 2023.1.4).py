from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

s=Service('C:/Users/Kryakena/Downloads/chromedriver-win64/chromedriver.exe')
driver = webdriver.Chrome(service=s)
driver.get("https://guru.qahacking.ru/")
time.sleep(3)
driver.set_window_size(1366,768)
driver.find_element(By.NAME, "mod_rscontact_full_name").clear()
driver.find_element(By.NAME, "mod_rscontact_full_name").send_keys("Крякена")
time.sleep(5)
driver.find_element(By.NAME, "mod_rscontact_email").clear()
driver.find_element(By.NAME, "mod_rscontact_email").send_keys("kryakozyabra@mail.com")
time.sleep(3)
driver.find_element(By.NAME, "mod_rscontact_mobile_phone").clear()
driver.find_element(By.NAME, "mod_rscontact_mobile_phone").send_keys("+79644568777")
time.sleep(3)
driver.find_element(By.NAME, "mod_rscontact_subject").clear()
driver.find_element(By.NAME, "mod_rscontact_subject").send_keys("Хочу пёсика в жёлтый горошек!")
time.sleep(3)
driver.find_element(By.ID, "mod-rscontact-submit-btn-91").click()
time.sleep(5)