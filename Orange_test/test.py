import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.implicitly_wait(10)
driver.find_element(By.CSS_SELECTOR,"input[name='username']").send_keys("Admin")
driver.find_element(By.CSS_SELECTOR,"input[name='password']").send_keys("admin123")
driver.find_element(By.CSS_SELECTOR,".orangehrm-login-button").click()

#Admin
driver.find_element(By.XPATH,"//div[@id='app']//aside[@class='oxd-sidepanel']/nav[@role='navigation']//ul[@class='oxd-main-menu']//a[@href='/web/index.php/admin/viewAdminModule']/span[.='Admin']").click()
driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[1]/header/div[2]/nav/ul/li[2]/span").click()
driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[1]/header/div[2]/nav/ul/li[3]/span").click()
driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[1]/header/div[2]/nav/ul/li[4]/span").click()
driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[1]/header/div[2]/nav/ul/li[5]/a").click()
driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[1]/header/div[2]/nav/ul/li[6]/a").click()
driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[1]/header/div[2]/nav/ul/li[7]/span").click()

#PIM
driver.find_element(By.XPATH,"//div[@id='app']//aside[@class='oxd-sidepanel']/nav[@role='navigation']//ul[@class='oxd-main-menu']//a[@href='/web/index.php/pim/viewPimModule']").click()
driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[1]/header/div[2]/nav/ul/li[1]/span").click()
driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[1]/header/div[2]/nav/ul/li[2]/a").click()
driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[1]/header/div[2]/nav/ul/li[3]/a").click()
driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[1]/header/div[2]/nav/ul/li[4]/a").click()

#LEAVE
driver.find_element(By.XPATH,"//div[@id='app']//aside[@class='oxd-sidepanel']/nav[@role='navigation']//ul[@class='oxd-main-menu']//a[@href='/web/index.php/leave/viewLeaveModule']").click()
driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[1]/header/div[2]/nav/ul/li[1]/a").click()
driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[1]/header/div[2]/nav/ul/li[2]/a").click()
driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[1]/header/div[2]/nav/ul/li[3]/span").click()
driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[1]/header/div[2]/nav/ul/li[4]/span").click()
driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[1]/header/div[2]/nav/ul/li[5]/span").click()

#TIME
driver.find_element(By.XPATH,"/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[4]/a/span").click()
driver.find_element(By.XPATH,"/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[2]/span").click()
driver.find_element(By.XPATH,"/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[3]/span").click()
driver.find_element(By.XPATH,"/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[4]/span").click()

#RECUIRTMENT
driver.find_element(By.XPATH,"/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[5]/a/span").click()
driver.find_element(By.XPATH,"/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[2]/a").click()

#My Info
driver.find_element(By.XPATH,"/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[6]/a/span").click()
driver.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[1]/div[2]/div[2]/a").click()
driver.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[1]/div[2]/div[3]/a").click()
driver.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[1]/div[2]/div[4]/a").click()
driver.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[1]/div[2]/div[5]/a").click()
driver.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[1]/div[2]/div[6]/a").click()
driver.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[1]/div[2]/div[7]/a").click()
driver.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[1]/div[2]/div[8]/a").click()
driver.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[1]/div[2]/div[9]/a").click()
driver.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[1]/div[2]/div[10]/a").click()

#Performance
driver.find_element(By.XPATH,"/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[7]/a/span").click()
driver.find_element(By.XPATH,"/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[3]/a").click()
driver.find_element(By.XPATH,"/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[4]/a").click()
driver.find_element(By.XPATH,"/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[1]/span").click()

#Dashboard
driver.find_element(By.XPATH,"/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[8]/a/span").click()

#Directory
driver.find_element(By.XPATH,"/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[9]/a/span").click()

#Maintenance
driver.find_element(By.XPATH,"/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[10]/a/span").click()
driver.find_element(By.XPATH,"/html/body/div/div[1]/div[1]/form/div[3]/div/div[2]/input").send_keys("admin123")
driver.find_element(By.XPATH,"/html/body/div/div[1]/div[1]/form/div[4]/button[2]").click()
driver.find_element(By.XPATH,"/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[2]/a").click()

#Claims
driver.find_element(By.XPATH,"/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[11]/a/span").click()
driver.find_element(By.XPATH,"/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[1]/span").click()
driver.find_element(By.XPATH,"/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[2]/a").click()
driver.find_element(By.XPATH,"/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[3]/a").click()
driver.find_element(By.XPATH,"/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[5]/a").click()

#Buzz
driver.find_element(By.XPATH,"/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[12]/a/span").click()

#Logout
driver.find_element(By.XPATH,"/html/body/div/div[1]/div[1]/header/div[1]/div[3]/ul/li/span/p").click()
driver.find_element(By.XPATH,"/html/body/div/div[1]/div[1]/header/div[1]/div[3]/ul/li/ul/li[4]/a").click()
